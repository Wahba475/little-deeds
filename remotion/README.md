# Remotion compositor

Puts the text layer (TikTok-style captions, pill, reference chip) and, when available locally, the voice track over the silent 3D scene.

1. Render the 3D layer without text: `QS='&nocaps=1' PAGE=dog.html python3 render.py dog_en video` (from the repo root), join the shots.
2. Copy it to `remotion/public/<file>.mp4` and export props from the data file (`export_props.py`).
3. `cd remotion && npm i && npx remotion render src/index.ts Short out/<id>.mp4 --props=public/<id>.json --browser-executable=/usr/bin/google-chrome --gl=swiftshader --concurrency=2`
4. If the voice mp3 is in `public/`, add `"voice": "<file>.mp3"` to the props and Remotion mixes it in; otherwise merge the voice in the ElevenLabs sandbox.
