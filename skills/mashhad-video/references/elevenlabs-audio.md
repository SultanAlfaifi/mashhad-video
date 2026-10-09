# Optional ElevenLabs narration and effects

Read when the user chooses ElevenLabs or generated audio is the selected production route. Narration remains optional, and Mashhad's music-free default still applies. This adapter is original integration guidance, not a bundled ElevenLabs skill or runtime.

## Select the available route

- **Connected plugin/MCP:** inspect the current tool schemas and available capabilities. If its `creative-studio` skill is available, read it for direct media generation. Use the existing connection; do not request a raw API key or install an SDK merely because API-oriented examples mention one. Honor a user-supplied voice ID exactly; if unavailable, report the result before choosing a substitute. Otherwise select an ID returned by the current voice-list tool, considering Arabic delivery, accent, tone, and available preview evidence. A voice name alone does not establish Arabic quality. Keep a particular project's voice choice in its brief, not as the skill's global default.
- **Application code or unavailable connector:** use the official Python `elevenlabs` or JavaScript `@elevenlabs/elevenlabs-js` SDK when this route and required setup are authorized. Keep `ELEVENLABS_API_KEY` in the local environment, outside source, output, and logs. Existing recordings or licensed effects remain valid alternatives when setup is unavailable.

Choose a model and parameters supported by the active tool, language, and account. A live schema or capability result takes precedence over remembered model names, parameter ranges, and old examples. Speech generation does not imply sound-effect generation or forced alignment is exposed by the same connector. Discover the relevant operation before promising it; do not use a music-generation tool as an effects substitute.

## Produce a coherent Arabic reading

Write the spoken script separately from the on-screen copy. Match the user's register, accent, emotional restraint, and intended audience. Use punctuation and selective diacritics to resolve ambiguous pronunciation, particularly names such as «مَشْهَد». Pronounce product names intentionally; omit URLs from speech when the visible link and QR already serve that purpose. Use inline performance directions only if the chosen model supports them.

For a short advert, prefer a continuous reading that preserves phrasing and tone. A brief sample can settle an uncertain voice or pronunciation before a longer run; it is unnecessary when an accepted voice already exists. Avoid assembling isolated words. If separate phrases are necessary, retain context and consistent settings, then listen across joins.

Generation spends credits. Use the user's existing authorization and requested scope; inspect an estimate when the tool provides it for a substantial run or variations. Record the request, returned flow/job identifiers, and generation count. After submission, check the existing job until completed or failed. An uncertain response is a reason to reconcile that job, not submit and charge for a second generation. Make any genuinely new take an explicit, bounded revision.

## Align the film to the recording

Obtain the completed playable/downloadable asset from the provider result and verify its format, duration, and decode. A flow URL, empty node, or queued job is not a finished voice track. Save the untouched recording with the working project.

Use returned timestamps, an available alignment operation, or measured phrase boundaries from the actual recording to build the cue map. When alignment is used, supply the matching transcript and check words near pauses and edits. Generated timestamps are candidates for review, not proof of synchronization. Do not invent word-level timings from character counts. If only phrase timing is established, use phrase reveals and label that precision honestly.

Place major reveals at relevant words and leave reading holds and a final CTA/QR hold. If duration conflicts with the brief, edit the script or adapt scene holds within scope. Preserve natural speech rather than silently speeding it up. Keep narration and effects as separate stems so a changed voice does not require rebuilding the visual composition.

## Design effects around the voice

For a soft, luxurious direction, request isolated, short, dry air movements and rounded tactile clicks. Describe the action, texture, length, and clean decay. Specify no speech, melody, rhythm, chimes, harmonic pad, or dramatic impact. These prompt constraints still require listening to the result. Silence is often preferable to another effect.

Place accents on visible actions, lower them under narration, and remove events competing with important consonants. Listen to the completed voice for pronunciation, cadence, emphasis, and synthetic artifacts; then listen to the final encoded mix for masking, sharp transients, tails, and sync. Decode, loudness, and peak checks are separate evidence. If listening is unavailable, deliver a clearly labeled preview and state that listening remains unperformed.

## Record rights and provenance

Keep the script, voice/model identifiers, generation date, asset reference, applicable service/plan rights, and final cue map with the project. Keep private account data and credentials out of public handoffs. The MIT license of ElevenLabs' instruction repository does not license generated audio, a voice identity, or the service itself. Confirm the intended use against current service terms; do not label all generated audio copyright-free or place it under Mashhad's MIT license automatically.

Official references checked 2026-10-09: [text-to-speech skill](https://github.com/elevenlabs/skills/tree/main/text-to-speech), [sound-effects skill](https://github.com/elevenlabs/skills/tree/main/sound-effects), [instruction repository MIT license](https://github.com/elevenlabs/skills/blob/main/LICENSE), [forced alignment](https://elevenlabs.io/docs/overview/capabilities/forced-alignment), and [generated-content publication rights](https://help.elevenlabs.io/hc/en-us/articles/13313564601361-Can-I-publish-the-content-I-generate-on-the-platform). The first two describe SDK/API workflows; connected-plugin authentication and operations are established by the installed connector.
