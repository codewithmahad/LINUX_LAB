#!/usr/bin/env python3
"""Rebuild the README's real sl/cowsay character animation.

On Ubuntu, install the commands and rendering tools first:
    sudo apt install sl cowsay tmux librsvg2-2 libcairo2 fonts-dejavu-core
Then, from the repository root:
    python3 assets/source/terminal-playground.py

Copyable commands shown in the animation:
    sl
    cowsay "mahad is dumb"

This runs sl in an isolated tmux server, captures its actual character screens,
and runs cowsay to obtain its actual stdout. The GIF is a styled replay of that
output with illustrative typing, colors, and timing, not a desktop recording.
The tmux socket is temporary, and no existing tmux session is accessed.
No network access or pip packages are needed. SL and COWSAY environment
variables may point to locally unpacked executables; /usr/games is also checked.

Train: sl by Toyoda Masashi, https://github.com/mtoyoda/sl
Copyright 1993,1998,2014 Toyoda Masashi (mtoyoda@acm.org).
Everyone is permitted to do anything on this program including copying,
modifying, and improving, unless you try to pretend that you wrote it.
i.e., the above copyright notice has to appear in all copies.
THE AUTHOR DISCLAIMS ANY RESPONSIBILITY WITH REGARD TO THIS SOFTWARE.

Cow: cowsay by Tony Monroe, https://github.com/tnalpgge/rank-amateur-cowsay
Copyright 1999-2000 Tony Monroe. Upstream is GPL-3.0; this script invokes cowsay
without bundling its program code. See ../README.md for all asset credits.
"""

import html
import importlib.util
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile
import time

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("terminal_demo", HERE / "terminal-demo.py")
demo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(demo)
demo.HEIGHT = 460
WIDTH, HEIGHT = demo.WIDTH, demo.HEIGHT
COLS, ROWS = 68, 20
COMMANDS = ["sl", 'cowsay "mahad is dumb"']


def executable(name):
    candidate = os.environ.get(name.upper()) or shutil.which(name)
    if not candidate:
        candidate = f"/usr/games/{name}"
    if not Path(candidate).is_file() or not os.access(candidate, os.X_OK):
        raise SystemExit(f"Missing executable {name}. Install it with sudo apt install sl cowsay tmux.")
    return str(Path(candidate).resolve())


def capture_train(sl):
    """Capture the real curses output, including moving wheels and steam."""
    snapshots = []
    with tempfile.TemporaryDirectory(prefix="linux-lab-sl-") as temporary:
        base = ["tmux", "-f", "/dev/null", "-S", f"{temporary}/capture.sock"]
        subprocess.run(base + ["new-session", "-d", "-s", "train", "-x", str(COLS),
                              "-y", str(ROWS), shlex.join([sl])], check=True)
        deadline = time.monotonic() + 20
        try:
            while time.monotonic() < deadline:
                result = subprocess.run(base + ["capture-pane", "-t", "train", "-p"],
                                        text=True, capture_output=True)
                if result.returncode:
                    break
                screen = result.stdout.splitlines()
                screen += [""] * (ROWS - len(screen))
                if any(line.strip() for line in screen):
                    snapshots.append(screen)
                time.sleep(0.12)
            else:
                raise RuntimeError("sl did not finish within 20 seconds")
        finally:
            subprocess.run(base + ["kill-server"], capture_output=True)
    if len(snapshots) < 15 or not any("[][]" in "\n".join(s) for s in snapshots):
        raise RuntimeError("The train capture is incomplete or sl failed to run")
    return snapshots


def frame(command, train=None, cow=None, cursor=False):
    drawing = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <title>Terminal</title>
  <desc>Actual character output from sl and cowsay mahad is dumb, replayed in a dark terminal.</desc>
  <rect width="{WIDTH}" height="{HEIGHT}" rx="16" fill="{demo.BACKGROUND}"/>
  <path d="M16 0h768a16 16 0 0 1 16 16v34H0V16A16 16 0 0 1 16 0" fill="{demo.HEADER}"/>
  <text x="30" y="31" fill="{demo.CREAM}" font-family="DejaVu Sans, sans-serif" font-size="14" letter-spacing="1">TERMINAL</text>
  <text x="770" y="31" text-anchor="end" fill="{demo.MUTED}" font-family="DejaVu Sans Mono, monospace" font-size="13">bash</text>
  <g font-family="DejaVu Sans Mono, monospace" font-size="25">
    <text x="30" y="91" fill="{demo.BLUE}">$</text>
    <text x="60.1" y="91" xml:space="preserve">{demo.colored_command(command)}</text>
  </g>''']
    if cursor:
        x = 60.1 + len(command) * 15.0513
        drawing.append(f'<rect x="{x:.2f}" y="71" width="2" height="25" fill="{demo.CREAM}"/>')
    if train:
        drawing.append('<g font-family="DejaVu Sans Mono, monospace" font-size="18" xml:space="preserve">')
        for row, line in enumerate(train):
            color = demo.MUTED if row < 4 else demo.BLUE if row < 11 else demo.MINT
            drawing.append(f'<text x="30" y="{113 + row * 16}" fill="{color}">{html.escape(line)}</text>')
        drawing.append('</g>')
    if cow:
        drawing.append('<g font-family="DejaVu Sans Mono, monospace" font-size="25" xml:space="preserve">')
        for row, line in enumerate(cow):
            color = demo.YELLOW if row < 3 else demo.MINT
            drawing.append(f'<text x="43" y="{139 + row * 30}" fill="{color}">{html.escape(line)}</text>')
        drawing.append('</g>')
    drawing.append('</svg>\n')
    return '\n'.join(drawing).encode()


def main():
    sl, cowsay = executable("sl"), executable("cowsay")
    if not shutil.which("tmux"):
        raise SystemExit("tmux is required to capture sl: sudo apt install tmux")
    train = capture_train(sl)
    result = subprocess.run([cowsay, "mahad is dumb"], text=True, capture_output=True, check=True)
    cow = result.stdout.splitlines()
    if "< mahad is dumb >" not in cow or not any("^__^" in line for line in cow):
        raise RuntimeError("Unexpected cowsay output")
    scenes = [(frame("", cursor=True), 40), (frame("s", cursor=True), 12),
              (frame("sl", cursor=True), 35)]
    scenes.extend((frame("sl", train=screen), 12) for screen in train)
    scenes.append((frame(""), 25))
    for end in range(3, len(COMMANDS[1]) + 3, 3):
        scenes.append((frame(COMMANDS[1][:end], cursor=True), 10))
    scenes[-1] = (scenes[-1][0], 35)
    final = frame(COMMANDS[1], cow=cow)
    scenes.append((final, 340))
    libraries = demo.native_rendering()
    demo.ASSETS.joinpath("terminal-playground.svg").write_bytes(final)
    frames = [(demo.rasterize(svg, libraries), delay) for svg, delay in scenes]
    demo.write_gif(frames, demo.ASSETS / "terminal-playground.gif")
    best_train = max(train, key=lambda screen: sum(len(line.strip()) for line in screen))
    demo.rasterize(frame("sl", train=best_train), libraries, Path("/tmp/linux-lab-playground-train.png"))
    demo.rasterize(final, libraries, Path("/tmp/linux-lab-playground-cow.png"))
    print(f"Captured {len(train)} real sl screens at {COLS}x{ROWS}; cowsay stdout:\n{result.stdout}")
    print(f"GIF: {len(frames)} frames, {sum(delay for _, delay in scenes) / 100:.2f}s, "
          f"{demo.ASSETS.joinpath('terminal-playground.gif').stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
