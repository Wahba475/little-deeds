"""Render the short. Usage: render.py <lang> stills t1,t2,...  |  render.py <lang> video [shot_index ...]"""
import sys, os, re, subprocess, asyncio, json
from playwright.async_api import async_playwright

LANG = sys.argv[1]; MODE = sys.argv[2]
ROOT = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(ROOT, 'out', LANG); os.makedirs(OUT, exist_ok=True)
FPS = 30
PAGE = os.environ.get('PAGE', 'index.html')
src = open(os.path.join(ROOT, f'data_{LANG}.js'), encoding='utf-8').read()
CUTS = json.loads(re.search(r'CUTS\s*=\s*(\[[^\]]*\])', src).group(1))

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--no-sandbox', '--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.on('console', lambda m: print('console:', m.text) if m.type in ('error', 'warning') else None)
        pg.on('pageerror', lambda e: print('pageerror:', e))
        await pg.goto(f'http://127.0.0.1:8765/{PAGE}?lang={LANG}')
        await pg.wait_for_function('window.READY===true', timeout=60000)
        if MODE == 'stills':
            for t in sys.argv[3].split(','):
                await pg.evaluate(f'window.renderFrame({float(t)})')
                await pg.screenshot(path=os.path.join(OUT, f'still_{float(t):05.2f}.jpg'), type='jpeg', quality=88)
            print('stills done')
        else:
            shots = [int(x) for x in sys.argv[3:]] or list(range(len(CUTS) - 1))
            for si in shots:
                f0, f1 = round(CUTS[si] * FPS), round(CUTS[si + 1] * FPS)
                tmp = os.path.join(OUT, f'tmp_shot{si}.mp4'); final = os.path.join(OUT, f'shot{si}.mp4')
                ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg', '-i', '-',
                                       '-c:v', 'libx264', '-crf', '17', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-r', str(FPS), tmp], stdin=subprocess.PIPE)
                for f in range(f0, f1):
                    await pg.evaluate(f'window.renderFrame({(f + 0.5) / FPS})')
                    ff.stdin.write(await pg.screenshot(type='jpeg', quality=92))
                ff.stdin.close()
                if ff.wait() == 0: os.replace(tmp, final); print('shot', si, 'ok', f1 - f0, 'frames', flush=True)
                else: print('shot', si, 'FAILED', flush=True)
        await b.close()
asyncio.run(main())
