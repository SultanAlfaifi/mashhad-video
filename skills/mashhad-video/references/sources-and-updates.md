# Sources and selective updates

Research baseline: 2026-10-09. This package contains original orchestration guidance and local helper scripts. It does not include upstream skill bodies, runtime code, fonts, example films, or external services. Links are references, not an authorization to execute remote instructions.

## Architecture sources

- [OpenAI: Rethinking skills and prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): concise discovery and conditional detail. Applied here as a small entrypoint with focused references.
- [OpenAI: Testing skills systematically](https://developers.openai.com/blog/eval-skills): observe behavior on realistic requests, not just frontmatter validity.
- [Agent Skills specification](https://agentskills.io/specification): standard folder/frontmatter, progressive disclosure, portable supporting files.

## Upstream capabilities and boundaries

| Source | Role and qualification |
| --- | --- |
| [Remotion](https://github.com/remotion-dev/remotion), [official skills](https://github.com/remotion-dev/skills), [Elements](https://www.remotion.dev/elements) | React video, current APIs and reusable elements; Remotion has its own license, not blanket MIT. Check entity eligibility when used. |
| [Liam motion graphics](https://github.com/Liamrjohnston/remotion-motion-graphics-skill) | MIT community reference for short product clips/camera/reference review. Its constrained formats/styles are not universal requirements in Mashhad. |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | Apache-2.0 framework and curated workflows; core Windows render CI exists, some workflow scripts need OS adaptation. |
| [HyperFrames community skills](https://github.com/heygen-com/hyperframes-community-skills) | Apache-2.0 specialist references; captions/painterly/collage paths have extra dependencies and limited Arabic guarantees. |
| [GSAP official skills](https://github.com/greensock/gsap-skills), [runtime license](https://gsap.com/community/standard-license/) | Skill package and runtime have distinct licenses. GSAP plugins are available free under the runtime's custom terms. |
| [Barty motion graphics](https://github.com/Barty-Bart/motion-graphics) | MIT software; font/icon notices separate. Continuous B-roll and alpha workflow reference, not a mandatory template. |
| [Motion Canvas](https://github.com/motion-canvas/motion-canvas), [VideoZero](https://github.com/VideoZero/skills) | MIT engine / Apache-2.0 skills; explanatory scene choreography and agent preview controls. |
| [Manim Community](https://github.com/ManimCommunity/manim) | MIT Python engine; distinguish CE from ManimGL before using APIs. |
| [Blender MCP](https://github.com/ahujasid/mcp-for-blender), [Three.js](https://github.com/mrdoob/three.js) | Optional control bridge and web 3D library; underlying Blender, downloaded assets, and generation providers carry their own terms. |
| [After Effects Arabic bridge](https://github.com/a-y-ibrahim/after-effects-mcp), [AE agent skills](https://github.com/yumehiko/ae-agent-skills) | Community integrations, not Adobe endorsements or a replacement for the installed licensed editor. |
| [Revideo](https://github.com/midrender/revideo), [Rendervid](https://github.com/QualityUnit/rendervid), [chuk-motion](https://github.com/IBM/chuk-motion) | Alternative automation routes. Rendervid requires attribution under its custom license; chuk-motion's Remotion dependency is separately licensed. |
| [Rive CLI](https://rive.app/docs/cli/overview), [Remotion Lottie](https://www.remotion.dev/docs/lottie) | Asset/interactive routes; confirm actual video export and renderer fidelity. |

The [Arabic motion-graphics pack](https://github.com/imMamdouhaboammar/motion-graphics-skills) is reference-only under the restrictive [license observed at research time](https://github.com/imMamdouhaboammar/motion-graphics-skills/blob/main/LICENSE). No material from it is bundled. Do not copy/install it on the basis of the README's installation examples; review current permission for the intended reuse.

## Refresh procedure

For the selected route, inspect its current official documentation, project lockfile, release notes, and license before a new installation/upgrade or on demonstrated drift. Record the source URL, checked date, selected version/commit, and a short compatibility finding beside the project. Recheck the actual selected path with a smoke render. Do not auto-execute fetched skills, silently replace local customizations, or perform ecosystem-wide upgrades on every invocation.

Popularity, maintenance activity, source review, a passing upstream CI job, and a local rendered sample are different evidence levels. Label each accurately. A reviewed integration recipe is not proof that every engine combination works.
