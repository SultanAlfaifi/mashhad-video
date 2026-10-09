# Arabic typography and sound timing

Read when Arabic, mixed-direction text, captions, narration, or any audio matters to the output.

## Preferred Arabic typeface

Default to **Thmanyah Sans (ثمانية Sans)** for most Arabic titles, body copy, captions, and product labels when the font is available with suitable permission. An explicit brand system, existing project typography, or requested alternative takes precedence. Serif variants are not the default.

Resolve the font from `THMANYAH_FONT_DIR` or an explicit user-provided location. The directory can point to `thmanyahsans/`, or to its parent containing that folder. The following filenames and OTF weight metadata were verified in a supplied family on 2026-10-09; verify the available files in each environment:

| Use | Weight | Exact file stem |
| --- | --- | --- |
| Body and longer captions | 400 | `thmanyahsans-Regular` |
| Labels and supporting emphasis | 500 | `thmanyahsans-Medium` |
| Headlines and short emphasis | 700 | `thmanyahsans-Bold` |
| Occasional large display type | 900 | `thmanyahsans-Black` |

Each stem exists as `otf/<stem>.otf` and `woff2/<stem>.woff2`. Prefer WOFF2 for browser compositions and OTF for a native renderer. Load the exact files; in CSS, register a consistent family alias such as `Mashhad Thmanyah Sans` with one `@font-face` per weight. Internal family names differ for Medium and Black, so system-font lookup alone may choose the wrong face. Avoid synthetic bold. Await font readiness before measuring or rendering text.

Check only the configured or supplied font location. If the font is unavailable, report that fact and choose an available Arabic-capable fallback consistent with the brief, unless exact typography is required. Do not search private home folders or assume a machine-specific path. The fonts are not bundled with this skill or installed into the OS. Record the font source and applicable permission separately; a portable handoff should describe the dependency without silently redistributing the files.

## Arabic is shaped text

Keep source text in logical reading order. Use the renderer's shaping and bidi support; do not reverse character arrays. Set the paragraph direction deliberately. Isolate embedded English product names, URLs, model identifiers, and number/currency runs as needed, rather than forcing the whole sentence into one direction. In HTML, use `dir="rtl"` for the Arabic block, tightly wrapped known-direction runs, and `bdi` or `dir="auto"` for unknown-direction content [1].

Letter-by-letter DOM splitting can break contextual joining and mark placement. Prefer word/phrase animation, line masks, or a reveal over a fully shaped text surface. Grapheme segmentation protects combining sequences but does not by itself preserve cursive joins between separately rendered spans. For a true calligraphic build, use shaped glyph geometry and an intentional stroke sequence; verify the resulting word visually [2].

Load the exact licensed font files and required weights before measuring layout or rendering. In Remotion, follow the active renderer's font-loading path; SVG text and browser text can have different font-loading behavior [3]. Preview Arabic and Latin at matched optical size. Check ascenders, descenders, vowel marks, joined forms, line spacing, fallback glyphs, punctuation, and actual numerals at final resolution.

Use a representative string such as `مَشْهَد — إطلاق المنتج (الإصدار 2.0) بسعر ١٢٩ ر.س.` and the video's real copy. Choose Western or Arabic-Indic numerals from the brief and audience, not a universal rule. A temporary typography probe should stay out of the delivered film. Recompose each requested aspect ratio; recentering a landscape layout is often insufficient.

## Time the voice before polishing motion

For narration-led work, obtain or generate the authorized voice track early. For optional ElevenLabs generation, use [elevenlabs-audio.md](elevenlabs-audio.md), including its connected-plugin route. Measure the resulting recording's actual duration, pauses, and stressed words. A word-count estimate helps drafting but does not establish the final timeline. If speech overruns a fixed duration, shorten the script or revise pacing naturally; do not silently accelerate the voice to rescue an overfull storyboard.

Build a cue map around meaning: phrase start, stressed word, reveal, breath, and transition. Align major motion to semantic beats and readable holds, without forcing a BPM grid. Leave some events silent. Keep enough stillness after the important reveal for recognition. For captions, use timing from the actual audio and verify phrase breaks, reading order, punctuation, and whether animation delays readability.

## Default to effects and nonmusical atmosphere

Use sparse transition effects, movement accents, tactile clicks, restrained impacts, and nonmusical environmental sound. Choose a sound because an object arrives, changes, travels, or occupies a space. Avoid a continuous bed when silence makes the message clearer. For a soft, luxurious brief, favor short air movements and low, rounded tactile clicks with clean tails; avoid sharp swishes and conspicuous synthetic hiss. Select among supplied recordings, licensed effects, optional generation, or procedural synthesis according to the listening result, rather than treating a generated waveform as inherently suitable. Retain the applicable provenance and permission.

Exclude melodies, chords, rhythmic instrumental loops, and tonal pads by default. Calling a track an “ambient background” does not make a musical drone or harmonic pad acceptable. Add music only after an explicit user request; do not revive it from an earlier draft. Preserve supplied/requested narration and its intelligibility. Do not add voices merely to fill silence.

Keep a cue list with time, purpose, asset path or generation script, provenance, and license/permission where applicable. For procedural sound, retain the synthesis source and any source samples; for stock effects, retain the source URL and license evidence. Music-free is a production choice, not a copyright-clearance guarantee. Removing a music stem is insufficient if it remains embedded in imported clips or a premixed track.

## Mix for the listening context

Make speech intelligible at ordinary playback volume when present. Keep effects and atmosphere subordinate to it. Avoid piercing transients, tiring hiss, heavy sub-bass, or repeated identical accents. Compare with sound on, sound off, and quiet playback. Inspect the final encode for clipped words, unintended clicks, abrupt tails, clipping, and audio/video offset. Listen to the final mix; a waveform or successful decode cannot establish pleasantness or the absence of music.

Measure loudness and true peaks when the destination specifies targets. FFmpeg's `loudnorm` supports measured normalization workflows [4]; normalization alone does not establish an intelligible mix. Do not raise sparse effects or quiet ambience to speech-like loudness merely to meet an invented universal LUFS rule. Record any required destination target. Unavailable requested voice generation or missing rights for an essential effect is a stated production gap, not evidence that sound was reviewed.

Primary references checked 2026-10-09: [1] [W3C bidi markup](https://www.w3.org/International/articles/inline-bidi-markup/); [2] [W3C Arabic layout, draft guidance](https://www.w3.org/TR/alreq/); [3] [Remotion fonts](https://www.remotion.dev/docs/fonts); [4] [FFmpeg loudnorm](https://ffmpeg.org/ffmpeg-filters.html#loudnorm).
