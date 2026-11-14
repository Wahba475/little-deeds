# Little Deeds

Renderer for the daily blocky-avatar Islamic reminder shorts (English and Egyptian Arabic).

- `night.html`: night bedroom scene (3:12 AM video). `dog.html`: street scene with a shot list `S` (the template for new scenarios).
- `data_<id>.js`: words with timings, shot cuts, pill text, reference chips.
- Render: `npm i`, `python3 -m http.server 8765 --bind 127.0.0.1 &`, then `PAGE=dog.html python3 render.py <id> stills 1,5,9` or `... video`.
- Hadith text is always copied by code from fawazahmed0/hadith-api (`align.py: hadith()`), never typed.
- `media/YYYY-MM-DD/`: silent renders, merged with the voice inside ElevenLabs.
