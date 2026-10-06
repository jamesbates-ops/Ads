#!/usr/bin/env python3
"""Assemble the Casedrops 'Saved the Night' cut: 33 clips + end card, cut to the song.

Usage: python3 -I assemble.py <workdir> <song.m4a>
Expects <workdir>/clips/shotNN.mp4 and <workdir>/stills/endcard.png.
Writes segments to <workdir>/build/ and the master to <workdir>/out/.
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

FPS = 24
W, H = 1080, 1920
NAVY = (19, 17, 33)
AMBER = (255, 183, 0)
FONT_BIG = '/usr/share/fonts/opentype/inter/Inter-Black.otf'
FONT_SMALL = '/usr/share/fonts/opentype/inter/Inter-Bold.otf'

# Cut points (seconds) from the song's embedded lyric timings; shot N runs CUTS[N-1]..CUTS[N].
CUTS = [0.0, 7.580, 13.005, 17.872, 22.021, 25.771, 29.441, 32.952, 38.617, 41.888,
        46.037, 53.138, 60.718, 66.000, 70.700, 75.479, 78.750, 82.819, 86.090,
        89.761, 93.431, 97.101, 100.771, 105.080, 108.511, 112.420, 115.691,
        120.000, 126.622, 130.293, 139.548, 146.729, 152.553, 161.500, 174.800]

# Chorus supers: shot -> (small line, big line)
CAPTIONS = {
    25: ('TOP-SHELF WINE', 'UP TO 80% OFF'),
    26: ('RIGHT TO YOUR DOOR', 'FREE DELIVERY'),
    27: ("DON'T LOVE IT?", 'GET A REFUND'),
}

FADE = 0.4  # dip between the last story shot and the end card


def frames(t):
    return round(t * FPS)


def run(cmd):
    subprocess.run(cmd, check=True)


def caption_png(path, small, big):
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    fs = ImageFont.truetype(FONT_SMALL, 46)
    fb = ImageFont.truetype(FONT_BIG, 96)
    ws = d.textlength(small, font=fs)
    wb = d.textlength(big, font=fb)
    box_w = int(max(ws, wb) + 2 * 56)
    box_h = 46 + 96 + 3 * 34
    x0 = (W - box_w) // 2
    y0 = 250
    d.rounded_rectangle([x0, y0, x0 + box_w, y0 + box_h], radius=36, fill=NAVY + (232,))
    d.text(((W - ws) / 2, y0 + 34), small, font=fs, fill=(255, 255, 255, 255))
    d.text(((W - wb) / 2, y0 + 34 + 46 + 22), big, font=fb, fill=AMBER + (255,))
    img.save(path)


def main():
    work, song = sys.argv[1], sys.argv[2]
    build = os.path.join(work, 'build')
    out = os.path.join(work, 'out')
    os.makedirs(build, exist_ok=True)
    os.makedirs(out, exist_ok=True)

    x264 = ['-c:v', 'libx264', '-preset', 'medium', '-crf', '16', '-pix_fmt', 'yuv420p', '-an']
    segs = []
    for shot in range(1, 34):
        n = frames(CUTS[shot]) - frames(CUTS[shot - 1])
        src = os.path.join(work, 'clips', f'shot{shot:02d}.mp4')
        seg = os.path.join(build, f'seg{shot:02d}.mp4')
        segs.append(seg)
        if os.path.exists(seg) and os.path.getmtime(seg) > os.path.getmtime(src):
            continue  # segment already built from this clip
        vf = (f'scale={W}:-2:flags=lanczos,crop={W}:{H},setsar=1,fps={FPS},'
              f'tpad=stop_mode=clone:stop_duration=2,trim=end_frame={n},setpts=PTS-STARTPTS')
        if shot == 33:
            vf += f',fade=t=out:st={n / FPS - FADE:.3f}:d={FADE}'
        if shot in CAPTIONS:
            png = os.path.join(build, f'cap{shot:02d}.png')
            caption_png(png, *CAPTIONS[shot])
            dur = n / FPS
            fc = (f'[0:v]{vf}[v];'
                  f'[1:v]format=rgba,fade=t=in:st=0.25:d=0.3:alpha=1,'
                  f'fade=t=out:st={dur - 0.45:.3f}:d=0.3:alpha=1[c];'
                  f'[v][c]overlay=0:0:shortest=1,format=yuv420p[o]')
            run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-loop', '1', '-framerate', str(FPS),
                 '-t', f'{dur:.3f}', '-i', png, '-filter_complex', fc, '-map', '[o]',
                 '-frames:v', str(n), *x264, seg])
        else:
            run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-vf', vf, '-frames:v', str(n), *x264, seg])

    # End card: slow push-in on the approved still, fading up from black.
    n = frames(CUTS[34]) - frames(CUTS[33])
    seg = os.path.join(build, 'seg34.mp4')
    vf = (f'scale={2 * W}:-2:flags=lanczos,crop={2 * W}:{2 * H},'
          f"zoompan=z='1+0.06*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS},"
          f'setsar=1,fade=t=in:st=0:d={FADE},fade=t=out:st={n / FPS - 1.0:.3f}:d=1.0')
    run(['ffmpeg', '-v', 'error', '-y', '-i', os.path.join(work, 'stills', 'endcard.png'),
         '-vf', vf, '-frames:v', str(n), *x264, seg])
    segs.append(seg)

    manifest = os.path.join(build, 'concat.txt')
    with open(manifest, 'w') as f:
        for s in segs:
            f.write(f"file '{s}'\n")
    picture = os.path.join(build, 'picture.mp4')
    run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', manifest, '-c', 'copy', picture])

    total = frames(CUTS[-1]) / FPS
    master = os.path.join(out, 'Casedrops_Saved_the_Night_9x16.mp4')
    run(['ffmpeg', '-v', 'error', '-y', '-i', picture, '-i', song,
         '-map', '0:v:0', '-map', '1:a:0', '-c:v', 'copy',
         '-af', f'afade=t=out:st={total - 0.6:.3f}:d=0.6', '-c:a', 'aac', '-b:a', '256k', '-ar', '48000',
         '-t', f'{total:.3f}', '-movflags', '+faststart', master])
    print(master)


if __name__ == '__main__':
    main()
