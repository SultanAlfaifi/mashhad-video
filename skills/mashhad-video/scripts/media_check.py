#!/usr/bin/env python3
"""Probe and fully decode a video. Mechanical checks never constitute visual QA.

Exit codes: 0 pass; 1 media/expectation failure; 2 tools/arguments/I/O failure;
3 timeout. Alpha requirement means decoded alpha channel, not necessarily nonopaque pixels.
"""
import argparse
import json
import math
import os
import pathlib
import re
import shutil
import subprocess
import sys
from fractions import Fraction


class CheckError(Exception):
    def __init__(self, kind, message, code):
        super().__init__(message)
        self.kind, self.code = kind, code


def positive(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("must be finite and positive")
    return number


def number(value):
    try:
        result = float(Fraction(str(value)))
        return result if math.isfinite(result) else None
    except (ValueError, ZeroDivisionError, TypeError):
        return None


def run(command, timeout, stage):
    try:
        result = subprocess.run(command, capture_output=True, text=True,
                                errors="replace", stdin=subprocess.DEVNULL, timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        raise CheckError("timeout", stage + " exceeded its timeout", 3) from exc
    except OSError as exc:
        raise CheckError("execution_error", stage + ": " + str(exc), 2) from exc
    return result


def aliases(a, b):
    if a.resolve() == b.resolve():
        return True
    try:
        return a.exists() and b.exists() and os.path.samefile(a, b)
    except OSError:
        return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=pathlib.Path)
    parser.add_argument("--json", dest="json_path", type=pathlib.Path)
    parser.add_argument("--expect-width", type=int)
    parser.add_argument("--expect-height", type=int)
    parser.add_argument("--expect-fps", type=positive)
    parser.add_argument("--expect-frames", type=int,
                        help="Exact positive decoded video frame count; performs a bounded ffprobe -count_frames pass")
    parser.add_argument("--expect-duration", type=positive, help="Seconds; checked against selected video stream")
    parser.add_argument("--duration-tolerance", type=positive,
                        help="Seconds; default max(one frame, 0.02 seconds)")
    parser.add_argument("--fps-tolerance", type=positive, default=0.01)
    parser.add_argument("--require-audio", action="store_true")
    parser.add_argument("--require-alpha", action="store_true",
                        help="Require a decoded alpha channel; report nonopaque pixels separately")
    parser.add_argument("--contact-sheet", type=pathlib.Path)
    parser.add_argument("--overwrite-outputs", action="store_true",
                        help="Allow replacing the explicitly named JSON/contact sheet outputs")
    parser.add_argument("--timeout", type=positive, default=120,
                        help="Per-subprocess timeout in seconds, including full decode")
    args = parser.parse_args()
    for value in (args.expect_width, args.expect_height):
        if value is not None and value <= 0:
            parser.error("expected dimensions must be positive")
    if args.expect_frames is not None and args.expect_frames <= 0:
        parser.error("--expect-frames must be a positive integer")
    source = args.file.resolve()
    report = {"schema_version": 1, "file": str(source), "status": "failed", "checks": [],
              "visual_qa": "not_performed", "full_decode": {"status": "not_performed"},
              "alpha": {"evidence": "not_checked", "decoded_channel": None,
                        "nonopaque_pixels_observed": None}}
    exit_code = 0
    safe_json = False

    def check(name, passed, actual=None, expected=None):
        report["checks"].append({"name": name, "passed": bool(passed),
                                 "actual": actual, "expected": expected})

    try:
        outputs = [path.resolve() for path in (args.json_path, args.contact_sheet) if path]
        for output in outputs:
            if aliases(source, output):
                raise CheckError("unsafe_output", "An output aliases the input; source will not be modified", 2)
            if output.exists() and not args.overwrite_outputs:
                raise CheckError("output_exists", str(output) + " exists; use --overwrite-outputs explicitly", 2)
        if len(outputs) == 2 and aliases(outputs[0], outputs[1]):
            raise CheckError("unsafe_output", "JSON and contact sheet paths must differ", 2)
        safe_json = True
        if not source.is_file():
            raise CheckError("input_missing", "Input is not a regular file", 2)
        ffprobe, ffmpeg = shutil.which("ffprobe"), shutil.which("ffmpeg")
        report["tools"] = {"ffprobe": ffprobe, "ffmpeg": ffmpeg}
        if not ffprobe or not ffmpeg:
            raise CheckError("missing_tool", "ffprobe and ffmpeg must both be available on PATH", 2)
        probe = run([ffprobe, "-v", "error", "-show_format", "-show_streams", "-of", "json", str(source)],
                    args.timeout, "ffprobe")
        if probe.returncode:
            raise CheckError("invalid_media", "ffprobe failed: " + probe.stderr[-4000:], 1)
        try:
            data = json.loads(probe.stdout)
        except ValueError as exc:
            raise CheckError("invalid_probe_output", str(exc), 2) from exc
        videos = [stream for stream in data.get("streams", [])
                  if stream.get("codec_type") == "video" and not stream.get("disposition", {}).get("attached_pic")]
        audios = [stream for stream in data.get("streams", []) if stream.get("codec_type") == "audio"]
        if not videos:
            raise CheckError("no_video", "No playable video stream found", 1)
        video = videos[0]
        stream_index = video["index"]
        fps = number(video.get("avg_frame_rate")) or number(video.get("r_frame_rate"))
        stream_duration = number(video.get("duration"))
        duration = stream_duration or number(data.get("format", {}).get("duration"))
        report["media"] = {"video_stream_index": stream_index, "video_stream_count": len(videos),
                           "audio_stream_count": len(audios), "width": video.get("width"),
                           "height": video.get("height"), "fps": fps,
                           "fps_basis": "avg_frame_rate" if number(video.get("avg_frame_rate")) else "r_frame_rate",
                           "duration": duration, "duration_basis": "video_stream" if stream_duration else "container_fallback",
                           "pixel_format": video.get("pix_fmt"), "codec": video.get("codec_name")}
        report["alpha"]["pixel_format_hint"] = video.get("pix_fmt")
        report["alpha"]["evidence"] = "pixel_format_metadata_only; decoded alpha not verified"
        base = [ffmpeg, "-hide_banner", "-nostdin", "-v", "error", "-xerror", "-err_detect", "explode", "-i", str(source)]
        decode = run(base + ["-map", "0:" + str(stream_index), "-map", "0:a?", "-f", "null", os.devnull],
                     args.timeout, "full_decode")
        report["full_decode"] = {"status": "passed" if decode.returncode == 0 and not decode.stderr.strip() else "failed",
                                 "returncode": decode.returncode, "diagnostics": decode.stderr[-4000:],
                                 "scope": "selected video stream and all audio streams, entire duration"}
        if decode.returncode or decode.stderr.strip():
            raise CheckError("decode_failed", "Full media decode failed", 1)
        if args.expect_frames is not None:
            report["frame_count"] = {"status": "not_completed", "video_stream_index": stream_index,
                                     "basis": "ffprobe -count_frames; decoded nb_read_frames, not nb_frames metadata"}
            counted = run([ffprobe, "-v", "error", "-count_frames", "-select_streams", str(stream_index),
                           "-show_entries", "stream=index,nb_read_frames", "-of", "json", str(source)],
                          args.timeout, "ffprobe_count_frames")
            if counted.returncode or counted.stderr.strip():
                raise CheckError("frame_count_failed", "Decoded frame counting failed: " + counted.stderr[-4000:], 1)
            try:
                counted_streams = json.loads(counted.stdout).get("streams", [])
                counted_video = next(item for item in counted_streams if item.get("index") == stream_index)
                raw_count = counted_video.get("nb_read_frames")
                if not re.fullmatch(r"[0-9]+", str(raw_count)):
                    raise ValueError("nb_read_frames is missing or not a nonnegative integer")
                actual_frames = int(raw_count)
            except (ValueError, TypeError, AttributeError, StopIteration) as exc:
                raise CheckError("frame_count_unavailable", "Cannot read decoded frame count: " + str(exc), 1) from exc
            report["frame_count"].update(status="read", actual=actual_frames)
            check("frames", actual_frames == args.expect_frames, actual_frames, args.expect_frames)
        for name in ("width", "height"):
            expected = getattr(args, "expect_" + name)
            if expected is not None:
                check(name, video.get(name) == expected, video.get(name), expected)
        if args.expect_fps is not None:
            check("average_fps", fps is not None and abs(fps - args.expect_fps) <= args.fps_tolerance,
                  fps, args.expect_fps)
        if args.expect_duration is not None:
            tolerance = args.duration_tolerance or max(1 / fps if fps and fps > 0 else 0.05, 0.02)
            report["duration_tolerance_seconds"] = tolerance
            check("duration", duration is not None and abs(duration - args.expect_duration) <= tolerance + 1e-8,
                  duration, args.expect_duration)
        if args.require_audio:
            check("audio_present", bool(audios), len(audios), "at least one decoded audio stream")
        if args.require_alpha:
            alpha_run = run(base + ["-map", "0:" + str(stream_index), "-an", "-vf",
                                   "alphaextract,format=gray,signalstats,metadata=print:key=lavfi.signalstats.YMIN:file=-",
                                   "-f", "null", os.devnull], args.timeout, "alpha_decode")
            minima = [float(value) for value in re.findall(r"lavfi\.signalstats\.YMIN=([0-9.]+)", alpha_run.stdout)]
            decoded = alpha_run.returncode == 0 and bool(minima) and not alpha_run.stderr.strip()
            report["alpha"].update(evidence="decoded_alpha_plane" if decoded else "alpha_extraction_failed",
                                   decoded_channel=decoded,
                                   nonopaque_pixels_observed=any(value < 255 for value in minima) if decoded else None,
                                   frames_inspected=len(minima), diagnostics=alpha_run.stderr[-2000:])
            check("alpha_channel", decoded, report["alpha"]["evidence"], "decoded alpha channel")
        if args.contact_sheet:
            if not duration or duration <= 0:
                raise CheckError("contact_sheet_failed", "A positive duration is required for contact sheet sampling", 1)
            args.contact_sheet.parent.mkdir(parents=True, exist_ok=True)
            filters = "fps=fps=" + str(9 / duration) + ":start_time=0:round=up,scale=320:-2,tile=3x3:nb_frames=9:padding=4:margin=4"
            sheet = run(base + ["-y" if args.overwrite_outputs else "-n", "-map", "0:" + str(stream_index),
                                "-an", "-vf", filters, "-frames:v", "1", str(args.contact_sheet.resolve())],
                        args.timeout, "contact_sheet")
            if sheet.returncode or not args.contact_sheet.is_file() or args.contact_sheet.stat().st_size == 0:
                raise CheckError("contact_sheet_failed", sheet.stderr[-4000:] or "No contact sheet produced", 1)
            report["contact_sheet"] = {"path": str(args.contact_sheet.resolve()),
                                       "evidence": "generated sampled frames; human/agent visual inspection still required"}
        failed = any(not item["passed"] for item in report["checks"])
        report["status"] = "failed" if failed else "passed"
        exit_code = 1 if failed else 0
        if failed:
            report["error"] = {"kind": "expectation_failed", "message": "One or more requested checks failed"}
    except CheckError as exc:
        exit_code = exc.code
        report["error"] = {"kind": exc.kind, "message": str(exc)}
    except OSError as exc:
        exit_code = 2
        report["error"] = {"kind": "io_error", "message": str(exc)}
    report["exit_code"] = exit_code
    output = json.dumps(report, ensure_ascii=False, indent=2)
    if args.json_path and safe_json:
        try:
            args.json_path.parent.mkdir(parents=True, exist_ok=True)
            with args.json_path.open("w" if args.overwrite_outputs else "x", encoding="utf-8") as handle:
                handle.write(output + "\n")
        except OSError as exc:
            report["status"] = "failed"
            report["error"] = {"kind": "output_write_failed", "message": str(exc)}
            report["exit_code"] = exit_code = 2
            output = json.dumps(report, ensure_ascii=False, indent=2)
    print(output)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
