Hero background video (optional)

To enable a looping hero video like IgniteAI:

1. Export two files from your editor or AI tool:
   - hero-loop.webm  (preferred — smaller, good quality)
   - hero-loop.mp4   (fallback for Safari / older browsers)

2. Place both files in this folder: assets/hero/

3. Recommended specs:
   - 1920×1080 or 2560×1440, 16:9
   - 10–20 second seamless loop
   - H.264 (mp4) + VP9/AV1 (webm)
   - No audio track (muted autoplay)
   - Keep file size under ~5–8 MB if possible (compress with HandBrake or similar)

4. Refresh the homepage — the site fades in the video when it loads successfully.
   Until files exist, the CSS animated mesh background is used instead.

Pitch video (section below hero):
  - pitch-90s.mp4 + pitch-90s.webm in this folder
  - 90-second elevator pitch, 16:9, with controls (not autoplay)

--- AI video generation tools (2025–2026) ---

Good for abstract / corporate loops (not talking-head):

  Runway (Gen-3 / Gen-4)     runwayml.com     — strong cinematic motion, image-to-video
  Kling AI                   klingai.com      — long clips, good for flythroughs
  Luma Dream Machine         lumalabs.ai      — clean 3D-ish motion
  Pika                       pika.art         — fast iterations on short loops
  Google Veo                 (via Gemini/Flow) — high quality when available
  OpenAI Sora                — check access; excellent for abstract scenes

Workflow that works well:
  1. Generate a still in Midjourney / DALL·E / Ideogram:
     "abstract white chrome data cubes, teal rim light, shallow depth of field, 16:9"
  2. Animate with Runway or Kling: slow camera push, 5–10s, seamless loop hint in prompt
  3. Edit loop point in DaVinci Resolve or CapCut (cross-dissolve first/last frame)
  4. Export webm + mp4, compress with HandBrake (CRF 28–32 for web)

Stock loops (no generation):
  coverr.co, pexels.com/videos — search "abstract technology", "data network", "3d cubes"
  Pick dark/teal-friendly clips; add a dark overlay in CSS if needed (already on .hero-bg::after)

Prompt ideas (abstract data / manufacturing tech, teal accents):
  "Slow cinematic flythrough of abstract white and chrome data cubes,
   soft depth of field, teal light accents, seamless loop, 4K, minimal, corporate"
