# Optional ElevenLabs narration and effects

Read when the user chooses ElevenLabs or generated audio is the selected production route. Narration remains optional, and Mashhad's music-free default still applies. This adapter is original integration guidance, not a bundled ElevenLabs skill or runtime.

## Connect only when the chosen audio route needs it

After the creative intake, use ElevenLabs when the user requests human-sounding AI narration. Discover the host's installed integration and exposed speech tools before asking for setup. An installed plugin label alone does not prove it is authenticated or can generate speech.

When the integration is missing or disconnected, ask in the user's language: "For human-sounding narration, please install or enable the official ElevenLabs plugin in your host and connect your ElevenLabs account. Tell me when the connection is ready." Add the Haytham recommendation only for an Arabic brief without a conflicting voice or accent preference; otherwise refer to the user's selected language and voice. Use the host's plugin discovery/setup surface when available; do not invent menu names or install commands. User sign-in belongs in the provider's connection flow, not in chat.

For a host using MCP directly, including Claude Code, consult the current [official hosted MCP guide](https://elevenlabs.io/docs/eleven-agents/operate/hosted-mcp). Its documented global endpoint is `https://api.elevenlabs.io/v1/mcp`, with OAuth; regional accounts use the endpoint specified in that guide. Follow the client's current connection process and verify its exposed speech tools. The old local `elevenlabs/elevenlabs-mcp` repository is archived and deprecated; do not make its old package/API-key installation the default.

When the user reports that connection is ready, perform a read-only capability/voice lookup. Reuse a working connection without asking them to reinstall or reconnect. If the integration is still unavailable, explain the specific missing capability and continue independent visual work; never claim narration was generated. Existing audio, another expressly chosen provider, or effects-only work remain valid routes.

## Select the available route

- **Connected plugin/MCP:** inspect the current tool schemas and available capabilities. If its `creative-studio` skill is available, read it for direct media generation. Use the existing connection; do not request a raw API key or install an SDK merely because API-oriented examples mention one. Honor a user-supplied voice ID exactly; if unavailable, report the result before choosing a substitute. Otherwise verify the Haytham preference below or select a suitable ID from the current voice-list tool. A voice name alone does not establish Arabic quality. Record the actual selected voice in the project's brief.
- **Application code or unavailable connector:** use the official Python `elevenlabs` or JavaScript `@elevenlabs/elevenlabs-js` SDK when this route and required setup are authorized. Keep `ELEVENLABS_API_KEY` in the local environment, outside source, output, and logs. Existing recordings or licensed effects remain valid alternatives when setup is unavailable.

Choose a model and parameters supported by the active tool, language, and account. A live schema or capability result takes precedence over remembered model names, parameter ranges, and old examples. Speech generation does not imply sound-effect generation or forced alignment is exposed by the same connector. Discover the relevant operation before promising it; do not use a music-generation tool as an effects substitute.

## Preferred Arabic voice: Haytham

The skill owner's chosen starting voice for Arabic human-sounding narration is **Haytham - Energetic, Warm and Cheerful**, listed by the connected library as **Haytham - Conversation**, with voice ID `IES4nrmZdUBHByLBde0P`. This is the voice used for the accepted Mashhad audition. Verify it through the current voice-list/search tool, using `Haytham` if a full-name search finds nothing. Do not silently substitute another Haytham variant or claim availability from this saved ID alone.

Its library metadata describes a warm, energetic Arabic male voice with an Egyptian accent. Prefer it for Arabic advertising when the user has not specified a conflicting voice or accent; an explicit Saudi, other dialect, language, or speaker choice takes precedence. The [official Arabic page](https://elevenlabs.io/text-to-speech/arabic) features this variant among its popular voices; this does not establish a universal usage ranking. [Open the exact voice](https://elevenlabs.io/app/voice-library?voiceId=IES4nrmZdUBHByLBde0P).

Match performance to the brief. For energetic advertising, use a currently supported expressive model and its documented delivery directions. The accepted example used `eleven_v3` with `[excited]` and `[confident]`; this is a reproducible reference, not a claim that v3 is always the newest or best model. Keep accepted voice/model settings for a continuation. For a fresh job, check available models and current prompting guidance. Never send audio tags to a model that reads them as spoken text, or confuse enthusiasm with shouting.

Offer a short audition on the actual script when the voice has not been accepted; do not repeatedly render a full video merely to audition speakers. Once the user accepts the voice or explicitly delegates selection, proceed within the existing generation authorization. Keep narration optional and preserve the music-free default.

## Produce a coherent Arabic reading

Write the spoken script separately from the on-screen copy. Match the user's register, accent, emotional restraint, and intended audience. Use punctuation and selective diacritics to resolve ambiguous pronunciation, particularly names such as «مَشْهَد». Pronounce product names intentionally; omit URLs from speech when the visible link and QR already serve that purpose. Use inline performance directions only if the chosen model supports them.

For a short advert, prefer a continuous reading that preserves phrasing and tone. A brief sample can settle an uncertain voice or pronunciation before a longer run; it is unnecessary when an accepted voice already exists. Avoid assembling isolated words. If separate phrases are necessary, retain context and consistent settings, then listen across joins.

Generation spends credits. Use the user's existing authorization and requested scope; inspect an estimate when the tool provides it for a substantial run or variations. Record the request, returned flow/job identifiers, and generation count. After submission, check the existing job until completed or failed. An uncertain response is a reason to reconcile that job, not submit and charge for a second generation. Make any genuinely new take an explicit, bounded revision.

## Align the film to the recording

Obtain the completed playable/downloadable asset from the provider result and verify its format, duration, and decode. A flow URL, empty node, or queued job is not a finished voice track. Save the untouched recording with the working project.

Use returned timestamps, an available alignment operation, or measured phrase boundaries from the actual recording to build the cue map. When alignment is used, supply the matching transcript and check words near pauses and edits. Generated timestamps are candidates for review, not proof of synchronization. Do not invent word-level timings from character counts. If only phrase timing is established, use phrase reveals and label that precision honestly.

A transcription tool that returns the original prompt, especially with unspoken direction tags intact, has not independently verified the recording. Do not count such an echo as pronunciation, word-timing, or listening evidence.

Place major reveals at relevant words and leave reading holds and a final CTA/QR hold. If duration conflicts with the brief, edit the script or adapt scene holds within scope. Preserve natural speech rather than silently speeding it up. Keep narration and effects as separate stems so a changed voice does not require rebuilding the visual composition.

## Design effects around the voice

For a soft, luxurious direction, request isolated, short, dry air movements and rounded tactile clicks. Describe the action, texture, length, and clean decay. Specify no speech, melody, rhythm, chimes, harmonic pad, or dramatic impact. These prompt constraints still require listening to the result. Silence is often preferable to another effect.

Place accents on visible actions, lower them under narration, and remove events competing with important consonants. Listen to the completed voice for pronunciation, cadence, emphasis, and synthetic artifacts; then listen to the final encoded mix for masking, sharp transients, tails, and sync. Decode, loudness, and peak checks are separate evidence. If listening is unavailable, deliver a clearly labeled preview and state that listening remains unperformed.

## Record rights and provenance

Keep the script, voice/model identifiers, generation date, asset reference, applicable service/plan rights, and final cue map with the project. Keep private account data and credentials out of public handoffs. The MIT license of ElevenLabs' instruction repository does not license generated audio, a voice identity, or the service itself. Confirm the intended use against current service terms; do not label all generated audio copyright-free or place it under Mashhad's MIT license automatically.

Official references checked 2026-10-09: [text-to-speech skill](https://github.com/elevenlabs/skills/tree/main/text-to-speech), [sound-effects skill](https://github.com/elevenlabs/skills/tree/main/sound-effects), [instruction repository MIT license](https://github.com/elevenlabs/skills/blob/main/LICENSE), [forced alignment](https://elevenlabs.io/docs/overview/capabilities/forced-alignment), and [generated-content publication rights](https://help.elevenlabs.io/hc/en-us/articles/13313564601361-Can-I-publish-the-content-I-generate-on-the-platform). The first two describe SDK/API workflows; connected-plugin authentication and operations are established by the installed connector.
