#!/usr/bin/env python3
"""Read-only local capability inventory. Availability is not render verification."""
import argparse
import json
import math
import pathlib
import shutil
import subprocess
import sys


PACKAGES = (
    "remotion", "@remotion/cli", "@remotion/renderer", "hyperframes",
    "@hyperframes/cli", "@motion-canvas/core", "@motion-canvas/ffmpeg",
    "revideo", "@revideo/core", "gsap", "three",
)


def read_manifest(path):
    if not path.is_file():
        return {"status": "absent", "path": str(path)}
    try:
        if path.stat().st_size > 1024 * 1024:
            return {"status": "too_large", "path": str(path)}
        value = json.loads(path.read_text(encoding="utf-8-sig"))
        if not isinstance(value, dict):
            raise ValueError("manifest must be an object")
        return {"status": "read", "path": str(path), "data": value}
    except (OSError, ValueError) as exc:
        return {"status": "unreadable", "path": str(path), "error": str(exc)}


def inspect_tool(name, timeout):
    found = shutil.which(name)
    result = {"path": found, "cli_available": bool(found), "engine_verified": False}
    if not found:
        result["status"] = "missing"
        return result
    argument = "-version" if name in ("ffmpeg", "ffprobe") else "--version"
    try:
        run = subprocess.run([found, argument], capture_output=True, text=True,
                             errors="replace", timeout=timeout, stdin=subprocess.DEVNULL)
        result.update(status="version_read" if run.returncode == 0 else "version_failed",
                      returncode=run.returncode,
                      version_output="\n".join((run.stdout or run.stderr).splitlines()[:3])[:2048])
    except subprocess.TimeoutExpired:
        result["status"] = "timeout"
    except OSError as exc:
        result.update(status="execution_failed", error=str(exc))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=pathlib.Path,
                        help="Inspect only this project's package.json and named local package manifests")
    parser.add_argument("--timeout", type=float, default=8, help="Per-command timeout in seconds")
    args = parser.parse_args()
    if not math.isfinite(args.timeout) or args.timeout <= 0:
        parser.error("--timeout must be finite and positive")
    report = {
        "schema_version": 1,
        "scope": "local CLI versions and explicitly selected project manifests; no installs or network",
        "interpreter": sys.executable,
        "engine_verification": "not_performed; run a representative render for each selected engine",
        "tools": {name: inspect_tool(name, args.timeout)
                  for name in ("node", "npm", "ffmpeg", "ffprobe", "python", "blender")},
    }
    if args.project:
        project = args.project.resolve()
        root = read_manifest(project / "package.json")
        manifest = root.pop("data", {})
        root["declared"] = {key: manifest[key] for key in
                            ("name", "version", "packageManager", "engines", "dependencies", "devDependencies")
                            if key in manifest}
        packages = {}
        for name in PACKAGES:
            item = read_manifest(project / "node_modules" / name / "package.json")
            data = item.pop("data", {})
            if data:
                item.update(name=data.get("name"), version=data.get("version"))
            item["engine_verified"] = False
            packages[name] = item
        report["project"] = {"path": str(project), "exists": project.is_dir(),
                             "manifest": root, "local_packages": packages}
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
