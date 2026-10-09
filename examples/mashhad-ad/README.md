# Mashhad ad — SFX-only source

This example produces the original 28-second, 1920×1080, 30 fps public demo, with a repository QR code and a stable closing frame for scanning. Its audio consists of original procedural transition swishes, muted clicks, and nonmusical ambience. It contains no music, narration, or external audio samples.

The later Haytham narration experiment is separate from this source. Running these commands reproduces the SFX-only route; it does not generate ElevenLabs speech or spend service credits. Arabic text inside the artwork is intentional creative content; the production documentation is in English.

## Render the example

Requirements: Node.js with Playwright/Chromium, FFmpeg/ffprobe, and Python with NumPy, Pillow, and ReportLab. Dependencies are declared in `package.json` and `requirements.txt`; rendering commands do not install them automatically. Existing installations can be selected through `PLAYWRIGHT_PATH`, `SHARP_PATH`, `JSQR_PATH`, and `FFMPEG`.

Obtain [Thmanyah Sans from its official source](https://font.thmanyah.com/), then set `THMANYAH_FONT_DIR` to the local `thmanyahsans` directory containing `woff2/`. Font files are excluded under the [Thmanyah license](https://font.thmanyah.com/licenses).

```powershell
$env:THMANYAH_FONT_DIR = 'D:/Fonts/thmanyah typeface/thmanyahsans'
python make_qr.py
python audio/compose_sfx.py
node render.cjs proof
node render.cjs full
node encode.cjs mashhad-ad-sfx.mp4
```

Images are written to `frames/`. Encoding refuses to overwrite an existing video. To render a particular frame range, run `node render.cjs range 630 840`; the final boundary is exclusive. Each image depends on its frame number, so scenes do not need to be rendered in sequence.

`film.js` contains the text and animation. `make_qr.py` generates `assets/repository-qr.png`, which points directly to `https://github.com/SultanAlfaifi/mashhad-video`. `verify-qr.cjs` uses jsQR to check decoded video frames at multiple resolutions. The procedural effects generator is `audio/compose_sfx.py`; `audio/audio-report.json` records signal measurements and provenance.

## Adapt it into a new video

Start with a brief in the user's language. Ask about unresolved purpose and audience, delivery format and duration, visual style or references, copy and brand assets, and sound. Skip settled choices. A good result requires adapting the creative direction and reviewing a render; replacing the title alone does not guarantee a professional advertisement.

For human-sounding Arabic AI narration, follow the [ElevenLabs audio route](../../skills/mashhad-video/references/elevenlabs-audio.md). Reuse a connected ElevenLabs plugin or MCP connector. If none is connected, ask the user to install and connect it through the host's supported setup before generating speech. For an MCP client, follow the official [hosted MCP connection guide](https://elevenlabs.io/docs/eleven-agents/operate/hosted-mcp). Do not request a separate API key when the connector provides the required tools.

For an energetic Arabic ad, start with the project owner's preferred voice, **Haytham – Conversation**, `IES4nrmZdUBHByLBde0P`, after verifying availability. Use another voice when the user requests it, and never silently substitute one. Preview a short passage if voice selection is unsettled; reuse an accepted voice without another audition gate. Align the animation to the actual recording and keep narration separate from the SFX. Generated speech has its own service and usage rights; it is not automatically covered by this example's MIT license.

## Rights

The original artwork, scripts, and procedural effects are © 2026 Sultan Alfaifi and use the repository's MIT license. External libraries and Thmanyah Sans have independent licenses; see the [root third-party notices](../../THIRD_PARTY_NOTICES.md). This example does not bundle fonts, engines, or vendored libraries.
