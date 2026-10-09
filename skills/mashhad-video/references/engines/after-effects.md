# After Effects adapter

Use when the user wants an editable `.aep`, already owns an Adobe workflow, or needs particular native effects/plugins. Continue the supplied project and preserve editability, expressions, layer names and media links. A generated MP4 alone does not satisfy an editable-project request.

Discover the actual After Effects and `aerender` executable locations and versions; inspect project footage, fonts, plugin dependencies and Render Queue settings. Do not infer a licensed installation from a community MCP README. Use a connected MCP only after discovering its actual tools and testing a harmless project read. JSX, application automation and MCP wrappers are alternatives, not mandatory simultaneous layers.

With `$aerenderExe` set to a verified executable and a prepared project whose queue/output module are inspected, Adobe documents these command shapes:

```powershell
& $aerenderExe -help
& $aerenderExe -project work/film.aep -comp Main -s 0 -e 89
```

Resolve composition display-start/frame indexing before adopting that range. Confirm output-module and render-settings template names exist locally; do not assume a template named in a tutorial exists on another machine. Without a verified output override, use only an inspected queue destination. A render can launch a new AE instance.

Drive expressions from composition time with seeded randomness where required. Replace live data dependencies with a captured authorized input set. Bake simulations or cache temporal effects when independent rendering would otherwise change the result. Document effects that need history, pre-roll or matching plugin versions. Bound loops and work area explicitly.

Use the [integration contract](../engine-selection.md) for imported/exported plates: resolution, pixel aspect, FPS, frame range, color working space, alpha interpretation and audio offset. Match AE footage interpretation to the source plate. Render an alpha-capable intermediate only through a verified output module; a `.mov` suffix does not guarantee alpha. Keep one final audio mix and check the project working space against the encoded delivery.

Inspect Arabic shaping and mixed-direction punctuation in AE itself. Review both high-motion frames and final encoded playback for missing fonts, expression errors, third-party watermarks, changed effects and alpha halos. Reopen the deliverable project to verify linked assets and render dependencies before declaring it editable and portable.

Primary source reviewed 2026-10-09: [Adobe automated rendering and aerender](https://helpx.adobe.com/after-effects/desktop/render-and-export/automate-rendering/automated-rendering-network-rendering.html). Commands were documentation-checked, not executed locally. Community wrappers require their own version/license review before reuse.
