"""Original deterministic, non-musical SFX for the 28-second Mashhad film.

Requires Python + NumPy and FFmpeg/ffprobe. No samples, network, synthesizer
oscillators, melodies, chords, bass notes, beats, or prior soundtrack input.
The generated work can be reused under this project's license; provenance is
documented, but no automated process guarantees a copyright outcome.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import numpy as np

SR = 48000
DURATION = 28.0
SEED = 7129069


def run(args: list[str], timeout: int = 180) -> subprocess.CompletedProcess:
    return subprocess.run(args, check=True, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=timeout)


def loudness(ffmpeg: str, path: Path) -> dict:
    result = run([ffmpeg, "-hide_banner", "-nostdin", "-i", str(path),
                  "-af", "loudnorm=I=-21:TP=-2:LRA=9:print_format=json",
                  "-f", "null", "-"])
    blocks = re.findall(r'\{\s*"input_i".*?\}', result.stderr, re.S)
    if not blocks:
        raise RuntimeError("FFmpeg did not return loudness measurements")
    raw = json.loads(blocks[-1])
    return {"integrated_lufs": float(raw["input_i"]),
            "true_peak_dbtp": float(raw["input_tp"]),
            "loudness_range_lu": float(raw["input_lra"]),
            "threshold_lufs": float(raw["input_thresh"])}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--ffmpeg", default=shutil.which("ffmpeg"))
    parser.add_argument("--ffprobe", default=shutil.which("ffprobe"))
    args = parser.parse_args()
    if not args.ffmpeg or not args.ffprobe:
        raise SystemExit("FFmpeg and ffprobe must already be available")
    output_dir = args.out_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    track = np.zeros((round(SR * DURATION), 2), dtype=np.float64)
    cues: list[dict] = []

    def noise(seconds: float, low: float, high: float, tilt: float = .7) -> np.ndarray:
        count = round(seconds * SR)
        frequencies = np.fft.rfftfreq(count, 1 / SR)
        spectrum = np.fft.rfft(rng.normal(0, 1, count))
        # Broad, smooth spectral slopes avoid resonant pitches and brittle hiss.
        hp = (frequencies / (frequencies + low)) ** 3
        lp = 1 / (1 + (frequencies / high) ** 6)
        color = (np.maximum(frequencies, 50) / 300) ** (-tilt / 2)
        colored = np.fft.irfft(spectrum * hp * lp * color, n=count)
        colored -= np.mean(colored)
        rms = np.sqrt(np.mean(colored ** 2))
        return colored / max(float(rms), 1e-12)

    def put(start: float, signal: np.ndarray, gain: float, pan: float,
            kind: str, description: str) -> None:
        first = round(start * SR)
        length = min(len(signal), len(track) - first)
        if first < 0 or length <= 0:
            raise ValueError("Cue extends outside the film")
        left = math.sqrt((1 - pan) / 2)
        right = math.sqrt((1 + pan) / 2)
        track[first:first+length] += signal[:length, None] * gain * np.array([left, right])
        cues.append({"start_seconds": start, "duration_seconds": length / SR,
                     "kind": kind, "description": description,
                     "pan": pan, "source": "original procedural filtered random noise"})

    # Deliberately irregular soft cues; no rhythmic grid and no notes.
    for index, at in enumerate([0.0, 3.0, 6.0, 10.0, 14.0, 18.0, 21.0]):
        seconds = [0.50, 0.60, 0.56, 0.68, 0.61, 0.65, 0.66][index]
        t = np.linspace(0, 1, round(seconds * SR), endpoint=False)
        envelope = (np.sin(np.pi * t) ** 2.4) * np.exp(-1.3 * t)
        # Quiet final reveal; no flourish that distracts from the QR code.
        amount = [0.085, 0.100, 0.090, 0.100, 0.085, 0.095, 0.065][index]
        signal = noise(seconds, 100, 1750 + index % 3 * 240, .85) * envelope
        put(at, signal, amount, [-.22, .18, -.12, .21, -.17, .14, 0][index],
            "soft_air_transition", "Brief broad-band air movement, no pitch")

        seconds = .20 if index != 6 else .25
        t = np.arange(round(seconds * SR)) / SR
        envelope = (1 - np.exp(-t / .006)) * np.exp(-t / .040)
        envelope *= np.minimum(1.0, (seconds - t) / .03)
        signal = noise(seconds, 48, 470, 1.1) * envelope
        put(at + .07, signal, .065 if index != 6 else .040, 0,
            "muted_noise_impact", "Small cushioned impact without bass oscillator")

    # Sparse secondary object cues are non-periodic and quieter than transitions.
    for at, pan in [(1.52, -.18), (4.38, .14), (7.74, -.12), (8.91, .12),
                    (11.41, -.10), (15.66, .16), (19.17, -.13)]:
        seconds = .105
        t = np.arange(round(seconds * SR)) / SR
        envelope = (1 - np.exp(-t / .0025)) * np.exp(-t / .016)
        envelope *= np.minimum(1.0, (seconds - t) / .012)
        signal = noise(seconds, 250, 2200, .65) * envelope
        put(at, signal, .037, pan, "tactile_tick", "Soft non-pitched object movement")

    # Short air beds, separated by actual digital silence. No continuous drone.
    for at, seconds in [(2.12, .58), (5.03, .55), (12.07, .76), (16.27, .77), (23.24, 4.56)]:
        t = np.linspace(0, 1, round(seconds * SR), endpoint=False)
        envelope = np.sin(np.pi * t) ** 2
        signal = noise(seconds, 70, 630, 1.3) * envelope
        put(at, signal, .00125 if at < 21 else .00072, 0,
            "restrained_air_ambience", "Very low, non-tonal air texture with zero-ended fade")

    track[0] = 0
    track[round(27.8 * SR):] = 0

    def write_pcm(path: Path, data: np.ndarray, temporary: Path) -> None:
        raw_path = temporary / "render.f32le"
        data.astype("<f4").tofile(raw_path)
        run([args.ffmpeg, "-hide_banner", "-nostdin", "-y", "-f", "f32le",
             "-ar", str(SR), "-ac", "2", "-i", str(raw_path), "-c:a", "pcm_s24le",
             "-metadata", "title=Mashhad - original non-musical sound effects",
             "-metadata", "comment=Procedural noise-only SFX; no borrowed samples; seed 7129069",
             str(path)])

    final_path = output_dir / "mashhad-sfx.wav"
    with tempfile.TemporaryDirectory(prefix="sfx-render-", dir=output_dir) as temp:
        temp_dir = Path(temp)
        draft_path = temp_dir / "measurement.wav"
        write_pcm(draft_path, track, temp_dir)
        initial = loudness(args.ffmpeg, draft_path)
        desired_gain_db = -21.0 - initial["integrated_lufs"]
        peak_headroom_db = -2.4 - initial["true_peak_dbtp"]
        applied_gain_db = min(desired_gain_db, peak_headroom_db)
        track *= 10 ** (applied_gain_db / 20)
        write_pcm(final_path, track, temp_dir)
        measured = loudness(args.ffmpeg, final_path)

        # Decode final encoded WAV, not just the source buffer.
        decoded_path = temp_dir / "decoded.f32le"
        run([args.ffmpeg, "-v", "error", "-nostdin", "-xerror", "-i", str(final_path),
             "-f", "f32le", "-acodec", "pcm_f32le", str(decoded_path)])
        decoded = np.fromfile(decoded_path, dtype="<f4").reshape(-1, 2)
        probe = json.loads(run([args.ffprobe, "-v", "error", "-show_streams", "-show_format",
                                "-of", "json", str(final_path)]).stdout)
        rms = float(np.sqrt(np.mean(decoded.astype(np.float64) ** 2)))
        maximum = float(np.max(np.abs(decoded)))
        checks = {
            "decoded_frames": len(decoded), "expected_frames": round(SR * DURATION),
            "duration_exact": len(decoded) == round(SR * DURATION),
            "sample_rate_48000": probe["streams"][0]["sample_rate"] == "48000",
            "channels_stereo": decoded.shape[1] == 2,
            "clipped_sample_count": int(np.count_nonzero(np.abs(decoded) >= 1)),
            "first_sample_zero": bool(np.all(decoded[0] == 0)),
            "last_200ms_zero": bool(np.all(decoded[-round(.2 * SR):] == 0)),
            "true_peak_below_minus_2_dbtp": measured["true_peak_dbtp"] <= -2,
            "decode_errors": 0,
        }
        if not all(checks[k] for k in ["duration_exact", "sample_rate_48000", "channels_stereo",
                                       "first_sample_zero", "last_200ms_zero", "true_peak_below_minus_2_dbtp"]):
            raise RuntimeError(f"Audio verification failed: {checks}")
        if checks["clipped_sample_count"]:
            raise RuntimeError("Clipped output samples")

        report = {
            "title": "Mashhad original SFX-only soundtrack",
            "duration_seconds": DURATION, "sample_rate": SR, "channels": 2,
            "encoding": "24-bit signed PCM WAV", "seed": SEED,
            "creation_method": "Deterministic NumPy random noise, broad spectral filtering, shaped envelopes and panning",
            "borrowed_samples": [], "prior_music_inputs": [], "music": False,
            "tonal_oscillators": False, "melody_chords_beats": False,
            "rights_note": "Original procedural composition for Mashhad; no borrowed recordings. This documents provenance, not a legal guarantee or automated copyright clearance.",
            "listening_review": "Not performed by this generating agent; technical measurements do not substitute for listening.",
            "loudness": measured, "applied_gain_db": round(applied_gain_db, 3),
            "sample_peak_dbfs": round(20 * math.log10(maximum), 3),
            "rms_dbfs": round(20 * math.log10(rms), 3),
            "checks": checks, "cues": sorted(cues, key=lambda c: c["start_seconds"]),
            "sha256": hashlib.sha256(final_path.read_bytes()).hexdigest(),
            "ffmpeg_version": run([args.ffmpeg, "-version"]).stdout.splitlines()[0],
        }
        (output_dir / "audio-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"output": str(final_path), "loudness": measured, "checks": checks}, indent=2))


if __name__ == "__main__":
    main()
