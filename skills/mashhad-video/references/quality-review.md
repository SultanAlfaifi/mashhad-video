# Review the rendered result

Read for a new film, substantial visual change, or delivery. Scale checks to the change. A local copy correction does not justify rebuilding the complete production pipeline.

## Keep reviews reproducible

Identify each meaningful revision with its source revision or snapshot, render settings, input assets, and output path. Preserve a usable previous version when experimenting. Associate findings with timecodes and evidence: `00:04.20, final MP4, Arabic vowel clipped above title; add top inset`. Keep open defects distinguishable from subjective preferences and accepted tradeoffs.

Review in this order when it saves work: meaning and sequence, composition and typography, motion and continuity, materials, sound, final encode. Do not polish a transition whose scene may be removed. Fix the most damaging issue first, render the affected range, and compare the same moments before and after. Expand checks only when dependencies or a discovered failure justify them. A shared font change affects more scenes than a local position change.

## Evidence has different scopes

| Evidence | What it establishes | What it does not establish |
|---|---|---|
| Build or type check | Code passes that check | Attractive or correct imagery |
| Media probe | Container, dimensions, duration, streams | Readable text or good pacing |
| Rendered frame/contact sheet | Composition at sampled timestamps | Continuous motion or sound |
| Played segment | Temporal behavior within that segment | Unwatched sections |
| Full playback with audio | Reviewed sequence and mix in that playback context | Every device/platform outcome |

State exactly what was inspected. If continuous playback or audio listening is unavailable, deliver the artifact with that review gap explicit. Do not claim “watched” from extracted frames, or a professional quality score from technical checks.

## Visual and temporal passes

Inspect first and last frames, important reading holds, transition neighborhoods, difficult Arabic text, matte edges, and dense compositions. Use final-size views plus enlarged crops for defects. A contact sheet should include event-driven samples, not only equal time intervals. Check overflow, unexpected font fallback, contrast over moving backgrounds, sharpness, banding, compression artifacts, unintended empty frames, and mismatched alpha/color between engines.

Play the changed scene with lead-in and follow-through at normal speed. Look for popping, drifting anchors, changing object identity, collisions, discontinuous velocity, long dead time, premature cuts, and simultaneous attention demands. Inspect slow motion only to diagnose; judge pacing at intended speed. Test seeking and rerendering a difficult timestamp when procedural state or randomness is involved. Remotion animation should be derived from the current frame rather than wall-clock side effects [1].

For a new complete film, review the final encoded file end to end, including the opening, last hold, and audio tail. Check intended crop and playback size. For a narrow revision, replay its affected segment and verify the resulting file's technical integrity; do broader review if shared timing, fonts, audio, or composition changed.

For the default music-free mix, inspect the cue list and listen for accidental music retained in imported media, melodic effects, harmonic pads, or rhythmic instrumental loops. Check effects for harsh transients, fatigue, repeated accents, balance, clean tails, and alignment with the visible action; preserve requested speech. Verify each effect's recorded provenance or permission. Technical audio checks cannot prove that the mix is pleasant, music-free, or cleared for use; state any missing listening or rights evidence explicitly.

For exact frame-based delivery, run `media_check.py final.mp4 --expect-width 1920 --expect-height 1080 --expect-fps 30 --expect-duration 10 --expect-frames 300`, adapting the actual spec. `--expect-frames` counts decoded frames; the duration check deliberately allows a small timestamp tolerance and is not an exact frame-count check. FPS checks compare the reported average, not every frame's spacing. Add `--require-audio` only when sound is required, and `--require-alpha` for an alpha channel; inspect whether transparency is meaningful and edges composite correctly.

## Aesthetic verdicts need reasons

Use concrete observations: “The camera moves while the key sentence arrives, splitting attention”; “The payoff has no contrast because every entrance uses the same acceleration.” Recommend a visible adjustment and compare the result. Automated metrics may detect defects; they cannot certify taste. Stop when the requested result works and remaining choices are preferences, while preserving any user's requested review cycle.

Primary reference checked 2026-10-09: [1] [Remotion animation model](https://www.remotion.dev/docs/animating-properties).
