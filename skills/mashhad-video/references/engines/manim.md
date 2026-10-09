# Manim adapter

Use Manim for mathematical relationships, scientific geometry, equation transformations, and explanatory animations that need explicit construction logic. Use it as the primary engine for a cohesive mathematical film or as a helper that renders a bounded diagram into another compositor.

Inspect the existing Python environment and Manim version without creating an environment or installing dependencies. Confirm the selected Cairo/OpenGL path and its local prerequisites. Check whether the scene actually needs TeX or Typst before introducing that toolchain. `Text` and mathematical text use different rendering paths; test the actual Arabic font/shaping path instead of assuming a successful formula proves Arabic support.

After confirming the chosen environment, these command shapes are documented. Replace the filename/class with real scene definitions; these are not commands to create missing files.

```powershell
python -m manim --version
python -m manim -ql scene.py Main
python -m manim -sqh scene.py Main
```

`-s` saves a final still and does not prove all intermediate frames. The `-n` option addresses animation numbers, not video frame numbers. Select FPS, resolution, output directory and format through the pinned version's CLI/configuration; check `render --help` rather than copying flags between versions. Newer `png-sequence` support must be checked against the installed version.

Make total duration finite. Seed randomness; use time-based, repeatable updater logic and fixed-step simulation when needed. A sequential scene can require replay from a known start to reproduce an arbitrary frame. For acceptance, compare decoded frame indices from a completed proof rather than presenting an animation index as a seek timestamp. Avoid frame-rate-dependent integration for physical meaning.

Apply the [integration contract](../engine-selection.md) to helper clips: pixel dimensions, FPS, frame count, alpha mode, color interpretation and audio offset. Verify any transparent MOV/WebM/sequence through the target importer. Keep scientific labels editable in source, and place final narration/music in one compositor to prevent duplicate tracks.

Validate the mathematics as well as appearance: invariants, units, scale, arrow direction and continuity through transformations. Inspect the smallest intended display size, moving equation correspondences, and the spoken explanation's timing. Play the final output; a clean terminal result cannot establish instructional clarity.

Primary sources reviewed 2026-10-09: [Manim CLI and configuration](https://docs.manim.community/en/stable/guides/configuration.html), [source and license](https://github.com/ManimCommunity/manim). Documentation syntax was checked; no local Manim runtime is implied.
