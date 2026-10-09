---
name: mashhad-video
description: "مَشْهَد: design, render, and refine motion-graphics videos, animated explainers, product films, and video overlays. Use for video creation or motion-design edits, including Arabic; not ordinary website animation."
license: MIT
metadata:
  author: "Sultan Alfaifi"
  version: "1.2.0"
---

# مَشْهَد — Mashhad

Turn the user's idea, assets, or existing footage into an intentional, editable film. Own creative direction, engine selection, scene production, sound, integration, and evidence-based review through one entry point. Speak in the user's language.

This is a portable Agent Skill for **Codex and Claude Code**. Its shared core is `SKILL.md`, relative references, and Python standard-library helpers; `agents/openai.yaml` is optional Codex UI metadata. Use the host's available file, shell, browser, and collaboration tools. No host-specific plugin, API, or multi-agent feature is required; sequential execution is supported. Renderer binaries and project dependencies remain separate prerequisites.

**Default audio is music-free:** use sparse transition effects, motion accents, and nonmusical ambient backgrounds. Do not add melodies, chords, rhythmic instrumental loops, or tonal pads unless the user explicitly requests music. Preserve requested narration. Sound effects also need original-source or license/permission provenance; music-free does not mean copyright-free. Read the sound guidance below whenever producing or changing audio.

## Begin with the actual job

Honor the chosen style, engine, existing project, and authorization. For a small revision, inspect and change the affected shot; preserve its source, timing, and surrounding design. Do not restart discovery or propose alternate engines without a concrete reason.

For new work, recover the message, audience, intended surface, exact copy, duration or voice track, assets, and constraints from the conversation and files. Ask only for missing information that materially changes the result; infer reversible choices and state them briefly. If creative direction is delegated, choose and continue. Do not make approval of every storyboard, frame, or render a universal requirement.

Inspect the selected project's dependencies and available tools. [inspect_environment.py](scripts/inspect_environment.py) is an optional read-only aid, not proof of a functioning renderer. Match commands to the actual OS and installed version. No engine, plugin, MCP server, asset provider, or paid service becomes available merely because this skill mentions it.

## Choose a coherent production route

Read [engine-selection.md](references/engine-selection.md) when a route is undecided. Use one primary compositor and the smallest useful set of specialist engines. Different tools may produce individual assets or shots, but one master timeline owns final duration and sound. Prefer an existing usable project. Engine choice follows the desired picture and editability, not repository popularity.

Load only the selected adapters:

| Job | Adapter |
| --- | --- |
| React video, product/UI films, captions, data-driven templates | [Remotion](references/engines/remotion.md) |
| HTML films, seekable GSAP motion, shaders, website-based promos | [HyperFrames + GSAP](references/engines/hyperframes-gsap.md) |
| Explanatory vector choreography and code/diagram animation | [Motion Canvas](references/engines/motion-canvas.md) |
| Mathematical/scientific animation | [Manim](references/engines/manim.md) |
| Physical 3D, procedural geometry, product lighting | [Blender + Three.js](references/engines/blender-three.md) |
| Native editable AE projects and existing compositions | [After Effects](references/engines/after-effects.md) |
| Batch/template rendering or embedding a video system | [Automation engines](references/engines/automation-engines.md) |
| Interactive/vector assets or existing animation assets | [Rive + Lottie](references/engines/rive-lottie.md) |

For a straightforward edit with existing media, using the existing editor or FFmpeg may be sufficient. Do not introduce a heavy framework just to change a crop or concatenate approved clips. If a needed runtime is missing, prepare independent design/source work and identify the specific setup needed. Use existing authorization rather than requesting it again.

## Direct before adding detail

For a new visual direction, read [art-direction.md](references/art-direction.md). Establish a visual thesis and representative styleframe before investing in a long render. Scale this to the job: a five-second label needs fewer artifacts than a narrated campaign film.

Use [motion-recipes.md](references/motion-recipes.md) for kinetic type, continuous UI morphing, data stories, documentary collage, depth captions, painterly motion, and procedural 3D. Select a visual mechanism that expresses the content; vary rhythm and staging within a consistent system. Sound, typography, space, and transition intent are first-class design decisions. Complexity and effect count are not quality metrics.

For Arabic or any audio work, read [arabic-and-audio.md](references/arabic-and-audio.md). Prefer **Thmanyah Sans** for most Arabic work when the licensed files are supplied through `THMANYAH_FONT_DIR` or a user-provided location; explicit brand/project choices take precedence. Build timing around meaning, reading holds, and the actual voice recording when supplied, without forcing a musical BPM grid. Preserve Arabic shaping and mixed-script direction; test the actual font and output rather than trusting a browser preview alone.

## Build and integrate

For multiple shots, engines, or collaborators, read [production-contract.md](references/production-contract.md). Store the compact brief, shot map, asset provenance, exact project versions, and work status beside the project. Use [project_manifest.py](scripts/project_manifest.py) to initialize or validate a frame-based manifest when useful. The manifest records decisions; it does not make creative decisions or authorize actions.

Render a representative difficult shot early. Verify the selected engine can deliver the requested text, materials, transparency, aspect ratio, and audio before building the full sequence. Keep randomness seeded, timing seekable, font loading explicit, and source paths stable. A preview and a final render must use the same composition logic.

Exchange specialist output through explicit media contracts: frame rate/timebase, frame count, dimensions, color/transfer, alpha interpretation, and audio policy. Check a short imported result in the master compositor before rendering the entire specialist scene. Animate one logical object across transitions only when its spatial and semantic continuity actually holds.

Delegate independent shots or review only when it saves time or improves quality. Give each contributor its own file ownership, shot contract, accepted styleframe, and deliverable. Keep overall art direction, master timeline, and final audio under one owner. Sequential work uses the same contracts when delegation is unavailable. See [collaboration-and-recovery.md](references/collaboration-and-recovery.md).

## Review the film, then deliver

Use [quality-review.md](references/quality-review.md) for a final film or substantive motion change. Distinguish technical checks, visual frame inspection, motion playback, and listening. A successful command or attractive still does not prove a good video. For a small edit, review the changed area and its joins instead of rerunning unrelated checks.

[media_check.py](scripts/media_check.py) can check metadata, full decode, exact frame count, required audio, and declared output expectations. Contact sheets help locate visual issues but do not inspect themselves. Automated results cannot certify taste, Arabic readability, temporal smoothness, or audio mix quality. Report any unperformed check explicitly.

Fix the highest-impact observed defect, re-render affected work, and compare. Set a concrete render/time budget appropriate to the request; when remaining work needs user direction or more budget, preserve a resumable project and state the exact limitation. Do not cycle endlessly to chase an invented perfect score.

Deliver the requested media, editable source, and a compact record of checks and unresolved limitations. Present rendered, visually reviewed, and user-approved states accurately. Explain the chosen route only to the extent useful to the user. Publishing, purchases, external uploads, and provider use follow the user's actual authorization.

## Sources and maintenance

The adapters are original integration guidance, not bundled engines or a merged copy of third-party skills. [sources-and-updates.md](references/sources-and-updates.md) records provenance, licensing distinctions, and selective refresh rules. Consult it before adding an upstream dependency or incorporating third-party material. Preserve license notices when permitted code/assets are reused; keep restricted material out of the package.

When improving Mashhad itself, use [evaluation.md](references/evaluation.md) and the [evaluation cases](references/evaluation-cases.json). Validate actual behavior on realistic tasks, including small edits and unavailable tools. Record measured evidence and make narrow corrections.
