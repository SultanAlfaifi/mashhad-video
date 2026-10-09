# Blender and Three.js adapter

Choose Blender when the shot needs convincing lighting, materials, modeled objects, simulations or elaborate camera work. Choose Three.js for suitable web-native 3D, procedural geometry and tighter integration with an existing browser compositor. Make a single hero shot first; 3D complexity is justified by its contribution to the idea.

For Blender, discover the actual executable/version, inspect the `.blend` and its dependencies, and identify CPU/GPU render availability. For Three.js, inspect the locked version, renderer backend, browser capabilities, asset loaders and existing render integration. Use a configured Blender MCP only when its tools are actually exposed; the community plugin is optional. External model-generation services are separate providers with separate authorization and cost.

Blender's documented command shape can render one proof frame after the file's settings and output location are checked:

```powershell
& $blenderExe -b work/shot.blend -f 10
```

Here `$blenderExe` must already contain a discovered executable path. Validate flags with its local help; command order matters because loading a file can replace prior settings. Current manual retrieval was unavailable in this review; the cited legacy manual confirms this longstanding shape, not new-version behavior.

Bake simulations and procedural dependencies before independent frame rendering. Frame 10 of a baked shot should not depend on whether frame 9 was previously viewed. Use explicit frame-derived camera/object transforms in Three.js; stop autonomous loops during capture and reset stateful mixers/simulations before replay. Remotion projects should use a compatible `@remotion/three` integration rather than competing render loops.

Follow the [integration contract](../engine-selection.md). For Blender plates, record resolution/FPS, frame numbering, view transform, exposure, color space and straight/premultiplied alpha. Avoid applying a filmic display transform twice after export. Use an agreed RGBA image sequence or verified intermediate codec; mix final audio in the primary compositor. Record warm-up and handles separately from the visible shot.

Inspect silhouettes, contact shadows, temporal noise, reflections, camera clipping and edge halos against light/dark backgrounds. Check a difficult frame at final quality before budgeting the full render. Validate actual render output, since the viewport can use different lights, samples or color settings.

Sources reviewed 2026-10-09: [Blender CLI, legacy manual](https://docs.blender.org/manual/en/2.80/advanced/command_line/render.html), [Three.js documentation](https://threejs.org/docs/), [Remotion Three integration](https://www.remotion.dev/docs/three), [community Blender MCP](https://github.com/ahujasid/mcp-for-blender). Local renderer compatibility remains to be tested per project.
