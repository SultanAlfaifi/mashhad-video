# HyperFrames and GSAP adapter

Choose HyperFrames for HTML/CSS compositions, layered editorial films, SVG motion, and layouts best expressed in the browser. Use GSAP as a timing/morphing library inside the chosen compositor. It is not a standalone MP4 exporter. An existing Remotion project can use compatible GSAP integration without adopting another engine.

Inspect the local package, project files and lockfile, Node version, browser, and FFmpeg availability. Current HyperFrames documentation lists Node 22+ and FFmpeg; verify the pinned release's actual requirements. Review startup scripts before execution. Its upstream workflows can update/install skills on demand: honor existing setup authorization and do not mistake those calls for read-only discovery. Inspect community skills individually, especially Bash assumptions in PowerShell environments.

Once the local CLI and required runtime are confirmed, the documented command shapes are:

```powershell
npx.cmd --no-install hyperframes preview
npx.cmd --no-install hyperframes render
```

Read local `render --help` before adding flags or assuming output names. Preserve an existing output until a replacement has been verified.

Build a paused timeline whose state can be reconstructed at `time = frame / fps`. `timeline.seek()` positions GSAP in seconds; explicitly define whether callbacks are suppressed and move essential scene state out of side-effect-only callbacks. Avoid autonomous CSS animations, ticker-driven particles, and random values generated during capture. Scrub forward, backward, and directly to the same time; the picture should agree. Treat fonts, images, shaders, and video decoding as readiness dependencies, not fixed sleeps.

Use the [integration contract](../engine-selection.md): exact pixel size/FPS/frame count, alpha interpretation, color metadata and audio offset. Confirm the installed exporter supports the intended transparent delivery; a transparent web canvas does not imply the encoded file has alpha. Keep final audio ownership with the primary compositor. For web color and final video, compare decoded color patches rather than assuming matching hexadecimal values imply matching output.

Validate both a difficult moving shot and a text-heavy Arabic shot. SplitText-style glyph animation can break connected letters; animate words/lines or shaped masks when necessary. Inspect scene joins, shadow clipping, asset loading and sync in the actual exported video.

Primary sources reviewed 2026-10-09: [HyperFrames repository and CLI](https://github.com/heygen-com/hyperframes), [GSAP seek](https://gsap.com/docs/v3/GSAP/Timeline/seek()/), [GSAP license](https://gsap.com/community/standard-license/). These are documented capabilities, not local runtime verification.
