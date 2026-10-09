# Rive and Lottie adapter

Use for reusable vector characters, logo motion, icons, and supplied interactive animation assets. Keep the original `.riv` or Lottie JSON when the user wants reusable source. A captured film is a separate deliverable from an interactive asset; choose both only when requested or useful to the stated task.

Inspect the supplied asset's license, embedded/external images and fonts, dimensions, timeline FPS/duration and available animation/state-machine names. Inspect the installed runtime version and browser/WASM readiness. Rive editor features and community assets can have different terms from open-source runtimes. Do not install a player, editor, plugin or export service merely to probe an asset.

For an existing Remotion project, inspect compatible `@remotion/lottie` or `@remotion/rive` before writing a new capture system. Lottie integration has feature/expression limitations, so prove the actual asset rather than inferring compatibility from valid JSON. These libraries do not supply a universal independent command-line video encoder.

For Lottie, disable autoplay and loop according to the finite shot. `goToAndStop(value, true)` addresses a frame in the asset's own timeline; convert from composition time when FPS differs and define whether subframes are used. Test shuffled seeks: expressions may retain state or flicker under random access.

For Rive, author a finite input/event trace. Use a controlled low-level runtime or supported compositor integration to advance the animation/state machine and artboard by deterministic increments. A state machine cannot generally be reproduced by setting only a timestamp; reset and replay the same events from time zero or a verified checkpoint. Avoid advancing from wall-clock time during frame capture. Wait for fonts/images and WASM before the first sampled frame.

Apply the [integration contract](../engine-selection.md): raster resolution, compositor FPS, finite frame count, loop seam, alpha mode, color interpretation and audio policy. Transparent vector art should remain transparent only in an alpha-capable export; test actual decoded edges. Route soundtrack ownership to the main compositor and document any captured embedded audio.

Compare native playback and final capture at matching timestamps. Inspect masks, gradients, strokes, text shaping and loop seams at final size. Check frame zero after restart and a repeated seek near a transition. If capture cannot reproduce interaction state, export a deterministic pre-rendered plate and document the preserved source separately.

Primary sources reviewed 2026-10-09: [Lottie runtime controls](https://github.com/airbnb/lottie-web), [Remotion Lottie limits](https://www.remotion.dev/docs/lottie), [Remotion Rive integration](https://www.remotion.dev/docs/rive), [Rive low-level API](https://rive.app/community/doc/low-level-api-usage/doctAfBY6v3P). No runtimes are bundled or locally validated here.
