# Remotion adapter

Use for React-based product films, typography, charts, captions, and repeatable branded variants. Favor an existing Remotion project over creating another compositor. Elements and community components are optional assets to inspect for fitness, rights, and dependencies; they are not a substitute for the film's visual direction.

Inspect `package.json`, lockfile, composition entry point, `remotion.config.*`, installed CLI and browser before rendering. Match all `@remotion/*` versions to the project's compatible Remotion version. A CLI can fetch a browser when none is available: select a verified existing browser path or use already-authorized setup. Check the [current license](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md) for the actual organization and usage.

After confirming local packages and setting `$browserExe` to a discovered executable, this documented command shape renders a finite 90-frame sample. Adapt the real entry point and composition ID; use a props file on Windows.

```powershell
npx.cmd --no-install remotion render src/index.ts Main work/proof.mp4 --frames=0-89 --props=work/props.json --browser-executable "$browserExe"
```

Drive visuals from the composition frame. Avoid wall-clock timers and accumulated mutable movement; seed procedural randomness. Wait for fonts and media readiness using the installed version's supported APIs. For GSAP integration, prefer compatible `@remotion/gsap`, which pauses and seeks its timeline from the frame. Do not combine independent tickers. Inspect native integration packages only if that visual actually needs Three.js, Lottie, or Rive.

Define FPS, dimensions and duration in composition metadata; keep the [integration contract](../engine-selection.md) alongside helper exports. Deliver an opaque MP4 when requested; choose a verified alpha-capable codec/pixel-format combination or PNG sequence for compositing. Specify color conversion deliberately and keep dialogue/music mixing in the primary compositor. Frame-range endpoints in the CLI are inclusive.

Validate a sparse set of shuffled frames for state drift, then play the proof at delivery speed. Inspect Arabic joining, bidirectional numbers, line wrapping, crop boundaries, blur and fine strokes after encoding. Review the final decoded video with audio; Studio success only confirms the preview path. Record the exact command, resolved versions, and output metadata.

Primary sources reviewed 2026-10-09: [render CLI](https://www.remotion.dev/docs/cli/render), [GSAP integration](https://www.remotion.dev/docs/gsap), [official skills](https://github.com/remotion-dev/skills). Command syntax was documentation-checked; this adapter alone is not a local render test.
