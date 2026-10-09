# Production contract

Use this for multiple shots, engines, or contributors. Keep a simple edit simple.

## Project artifacts

Keep these next to the video source, adapting names to an existing project:

- `brief.md`: one audience, intended takeaway, exact supplied copy, format/duration, assets, constraints, chosen visual language, unresolved choices. Record the music-free default, requested narration, and any explicit audio override. Separate verified facts from proposed copy.
- `mashhad.json`: delivery specification, frame-based shot map, primary engine, asset provenance, dependency versions, and evidence paths. Initialize with `scripts/project_manifest.py new`; validate after timing changes.
- `shots/<id>/`: owned editable source and intermediate renders. Keep master source and audio under one owner.
- `review/`: representative frames/contact sheets, playback notes with timestamps, technical JSON, and known issues.

The manifest is a production ledger, not a universal intermediate language that can compile into every engine. Each engine retains its native editable source. An adapter defines how its output joins the film.

## Timing

The master uses integer frame indices and a rational FPS `{num, den}`. Time in seconds is `frame * den / num`; frame ranges are half-open `[start, start + duration)`. Avoid accumulated floating-point seconds when joining shots. Audio uses its own sample clock; calculate placement from the master timebase and check final drift.

Base shots collectively cover the intended timeline. Deliberate empty space is an explicit designed hold, not an unrecorded gap. Base overlaps require an explicit transition entry giving the participating shot IDs and its exact start/duration. Overlays can overlap freely but must stay within the film. Transition handles are outside a shot's visible range and must not silently increase the final duration.

When voice is supplied, measure its duration and place meaningful reading/visual holds around it. A requested fixed duration that cannot fit the supplied speech is a real content decision; explain the conflict instead of speeding speech until unintelligible or silently cutting words.

## Media handoff

Agree on these before a specialist render:

| Field | Required decision |
| --- | --- |
| Geometry | width, height, pixel aspect, crop/safe area and visible framing |
| Time | exact rational FPS, visible frame count, head/tail handles |
| Color | primaries, transfer and range; an SDR BT.709 delivery can be a practical choice when appropriate, never relabel HDR as SDR |
| Alpha | none/straight/premultiplied, container/codec and edge treatment |
| Audio | silent picture asset, or explicitly mapped channels, sample rate, and SFX/ambience/narration role; music only when explicitly requested |
| Source | native editable source, assets/font references, engine version and render command |

Prefer lossless image sequences or a tested mezzanine codec between engines. H.264 MP4 is normally a final delivery choice, not a transparent overlay format. A codec's support for alpha does not establish that the pixels contain meaningful transparency. Import a short sample over both light and dark backgrounds to expose premultiplication fringes.

Keep the master audio mix in one place to avoid doubled narration or effects. Render helper visuals silently unless their audio is deliberately included; inspect imported audio for embedded music before using it in a music-free mix. Keep effects, nonmusical ambience, and requested narration separable when useful. Check sample rate/channel handling at final mix. Record any tone mapping, color conversion, retiming, or resampling that changes the source.

## Provenance and status

For each external asset, including sound effects, atmosphere, and fonts, retain the source and applicable license/permission; distinguish user-supplied, original procedural, retrieved, and generated material. Original procedural audio should retain its generation source and any sample inputs. Music-free is not a rights clearance. Keep credentials out of manifests and logs. Record actual installed/pinned versions in `versions`, using `unknown` until inspected.

Useful statuses are `planned`, `source_ready`, `rendered`, `reviewed`, and `approved`. A rendered shot has a real media file; reviewed has a review record; approved means the user actually approved it. Approval is not required for routine progress unless the user's workflow calls for it.

## Tools

`project_manifest.py new <file> --title <title> --engine <engine> --width 1920 --height 1080 --fps 30/1 --frames 300` writes a new one-shot manifest without overwriting existing work.

`project_manifest.py validate <file> --check-files` checks structural/timing invariants and local evidence paths. It does not validate the native engine source or inspect media content. Use `media_check.py` and direct visual/audio review for those layers.

Each shot has `id`, `engine`, `layer` (`base` or `overlay`), `start_frame`, `duration_frames`, and `status`. Add path fields as evidence becomes available: `source` from `source_ready`, `media` from `rendered`, `review` from `reviewed`, and `approval` only for real user approval. Paths are relative to the manifest or absolute; a review path can point to a small JSON or text record. Keep paths portable when packaging the project. Extra native-engine fields are allowed but are not interpreted by this helper.

A transition uses `{ "from": "shot-01", "to": "shot-02", "start_frame": 140, "duration_frames": 10 }` when those two base shots overlap exactly on `[140,150)`. Assets use `id`, `provenance`, and an optional local `path`; add source URL and license fields when applicable. The helper checks recorded evidence paths when requested; it cannot establish that their contents are truthful or that a license permits the intended use.
