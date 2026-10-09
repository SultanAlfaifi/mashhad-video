# Motion Canvas and VideoZero adapter

Use for explanations whose meaning is carried by connections, diagrams, geometric transformations, and coordinated object movement. The generator-based scene model can make complex timing readable. Keep a working Motion Canvas project; do not translate it into React merely to satisfy a default preference.

Inspect installed `@motion-canvas/*` packages, Vite configuration, scene registration, project settings, and exporter. Preview FPS/scale may differ from rendering FPS/scale. Read the actual package scripts before invoking `npm.cmd start`; there is no universal command here that guarantees a final MP4. The core image-sequence exporter and FFmpeg exporter have different setup and output implications.

VideoZero's optional agent tooling provides editor seeking, screenshots and scene inspection. It requires its project plugin/client integration and a connected browser; it is not automatically present in every Motion Canvas project. When verified installed and already running on a discovered localhost port, inspect its documented status endpoint before commands. Do not invent an MCP server or assume a fixed port. Keep the control endpoint local.

For temporal reproducibility, derive changing properties through signals/tweens evaluated by the scene timeline. Seed procedural content and resolve assets before the rendered interval. Reconstruct a scene before an arbitrary seek when its logic depends on generator history; do not pretend a stateful generator is a pure random-access function. Compare direct seek, replay-from-start, and final-render frames on the same checkpoints.

Export a finite range with known first/last-frame semantics. Apply the [integration contract](../engine-selection.md): dimensions, rational FPS, frame count, alpha, color interpretation, and audio ownership. Prefer a numbered RGBA sequence for specialist diagram overlays when the configured exporter cannot prove transparent video support. Describe the sequence's sampling FPS explicitly; PNG files carry no timeline. Mux or mix narration once in the primary compositor and verify imported duration at joins.

Review line weights after downscaling, anchor/arrow attachment while objects move, graph labels at camera extremes, and Arabic shaping in actual Canvas text. Inspect the exported scene at delivery speed for unfinished threads, unintended pauses, offscreen content, and missing frames. A screenshot or successful HTTP render trigger is not proof that export finished.

Primary sources reviewed 2026-10-09: [Motion Canvas rendering](https://motioncanvas.io/docs/rendering/), [quickstart](https://motioncanvas.io/docs/quickstart/), [VideoZero repository](https://github.com/VideoZero/skills), [agent integration and HTTP API](https://github.com/VideoZero/skills/blob/main/motion-canvas-agent/SKILL.md). No VideoZero tooling is bundled by this adapter.
