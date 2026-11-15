"""Export Remotion props from a renderer data file: python3 export_props.py ../data_dog_en.js dog_en_scene.mp4 public/dog_en.json"""
import re, json, sys
js, video, out = sys.argv[1:4]
s = open(js, encoding='utf-8').read()
words = json.loads(re.search(r'WORDS = (\[.*?\]);\n', s, re.S).group(1))
dur = float(re.search(r'DURATION = ([\d.]+)', s).group(1))
pill = re.search(r'PILL = "([^"]*)"', s)
refs = re.search(r'REFS = (\[.*?\]);', s, re.S)
json.dump({'video': video, 'duration': dur, 'words': words, 'pill': pill.group(1) if pill else '',
           'refs': json.loads(re.sub(r'(\w+):', r'"\1":', refs.group(1))) if refs else [], 'rtl': 'RTL = true' in s},
          open(out, 'w', encoding='utf-8'), ensure_ascii=False)
print('wrote', out)
