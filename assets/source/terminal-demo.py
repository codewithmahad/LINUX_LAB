#!/usr/bin/env python3
"""Rebuild the README's animated command replay and static SVG.

Run from the repository root: python3 assets/source/terminal-demo.py
Requires Python 3, Bash, librsvg 2, Cairo, and DejaVu Sans Mono (Ubuntu/Debian).
No pip packages are needed. Commands execute in chapter 01 and their actual
stdout supplies the frames. The typing timing is illustrative: this is a
rendered replay, not a desktop screen recording. No network access is used.
"""

import ctypes as C
import html
from pathlib import Path
import re
import struct
import subprocess

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"
CWD = ROOT / "learning/bash-scripting/01-shell-and-script-basics"
WIDTH, HEIGHT = 800, 348
BACKGROUND = "#1E1E1E"
HEADER = "#252526"
CREAM = "#D4D4D4"
MINT = "#B5CEA8"
BLUE = "#569CD6"
MUTED = "#9DA3AB"
YELLOW = "#DCDCAA"
PEACH = "#CE9178"
COMMANDS = ["bash hello.sh", "echo $((17 % 5))", '(( 20 > 15 )); echo "$?"']
EXPECTED = ["Hello From Bash", "2", "0"]


def capture_outputs():
    outputs = []
    for command, expected in zip(COMMANDS, EXPECTED):
        result = subprocess.run(
            ["bash", "--noprofile", "--norc", "-c", command],
            cwd=CWD, text=True, capture_output=True, check=True,
        )
        output = result.stdout.rstrip("\n")
        if output != expected or result.stderr:
            raise RuntimeError(f"Unexpected command output: {command!r}: {result!r}")
        outputs.append(output)
    return outputs


def colored_command(value):
    """Keep command text intact while adding familiar editor syntax colors."""
    parts = []
    for token in re.findall(r'"[^\"]*(?:"|$)|[a-zA-Z_][\w.-]*|\d+|[^\w\"]+', value):
        color = CREAM
        if token in {"bash", "echo", "sl", "cowsay"}:
            color = YELLOW
        elif token.startswith('"'):
            color = PEACH
        elif token.isdecimal():
            color = MINT
        elif "$" in token or "((" in token or "))" in token:
            color = BLUE
        parts.append(f'<tspan fill="{color}">{html.escape(token)}</tspan>')
    return "".join(parts)


def svg_frame(lines, cursor_row=None, cursor_column=0):
    drawing = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <title>Three real Bash commands from Linux Lab</title>
  <desc>In chapter 01, bash hello.sh prints Hello From Bash. Integer remainder 17 % 5 prints 2. A true arithmetic comparison returns exit status 0.</desc>
  <rect width="800" height="348" rx="16" fill="{BACKGROUND}"/>
  <path d="M16 0h768a16 16 0 0 1 16 16v34H0V16A16 16 0 0 1 16 0" fill="{HEADER}"/>
  <text x="30" y="31" fill="{CREAM}" font-family="DejaVu Sans, sans-serif" font-size="14" letter-spacing="1">TERMINAL</text>
  <text x="154" y="31" fill="{MUTED}" font-family="DejaVu Sans, sans-serif" font-size="13">first commands</text>
  <text x="770" y="31" text-anchor="end" fill="{MUTED}" font-family="DejaVu Sans Mono, monospace" font-size="13">bash · Linux_LAB</text>
  <g font-family="DejaVu Sans Mono, monospace" font-size="26">''']
    for row, (value, is_command) in enumerate(lines):
        y = 91 + row * 37
        if is_command:
            drawing.append(f'<text x="30" y="{y}" fill="{BLUE}">$</text>')
            drawing.append(f'<text x="61.31" y="{y}" xml:space="preserve">{colored_command(value)}</text>')
        else:
            drawing.append(f'<text x="30" y="{y}" fill="{MINT}">{html.escape(value)}</text>')
    drawing.append("</g>")
    if cursor_row is not None:
        x = 61.31 + cursor_column * 15.6543
        y = 71 + cursor_row * 37
        drawing.append(f'<rect x="{x:.2f}" y="{y}" width="2" height="25" fill="{CREAM}"/>')
    drawing.append("</svg>\n")
    return "\n".join(drawing).encode()


def native_rendering():
    rsvg = C.CDLL("librsvg-2.so.2")
    cairo = C.CDLL("libcairo.so.2")
    gobject = C.CDLL("libgobject-2.0.so.0")
    signatures = [
        (rsvg, "rsvg_handle_new_from_data", [C.c_char_p, C.c_size_t, C.c_void_p], C.c_void_p),
        (rsvg, "rsvg_handle_render_cairo", [C.c_void_p, C.c_void_p], C.c_int),
        (cairo, "cairo_image_surface_create", [C.c_int, C.c_int, C.c_int], C.c_void_p),
        (cairo, "cairo_create", [C.c_void_p], C.c_void_p),
        (cairo, "cairo_image_surface_get_data", [C.c_void_p], C.c_void_p),
        (cairo, "cairo_image_surface_get_stride", [C.c_void_p], C.c_int),
        (cairo, "cairo_surface_flush", [C.c_void_p], None),
        (cairo, "cairo_surface_write_to_png", [C.c_void_p, C.c_char_p], C.c_int),
        (cairo, "cairo_destroy", [C.c_void_p], None),
        (cairo, "cairo_surface_destroy", [C.c_void_p], None),
        (gobject, "g_object_unref", [C.c_void_p], None),
    ]
    for library, name, arguments, result in signatures:
        fn = getattr(library, name)
        fn.argtypes, fn.restype = arguments, result
    return rsvg, cairo, gobject


def make_palette():
    base = tuple(bytes.fromhex(BACKGROUND[1:]))
    colors = [base]
    for color in [HEADER, CREAM, MINT, BLUE, MUTED, YELLOW, PEACH]:
        rgb = tuple(bytes.fromhex(color[1:]))
        for step in range(1, 19):
            shade = tuple(round(a + (b - a) * step / 18) for a, b in zip(base, rgb))
            if shade not in colors:
                colors.append(shade)
    return colors + [base] * (128 - len(colors))


PALETTE = make_palette()
COLOR_CACHE = {}


def rasterize(svg, libraries, png=None):
    rsvg, cairo, gobject = libraries
    handle = rsvg.rsvg_handle_new_from_data(svg, len(svg), None)
    surface = cairo.cairo_image_surface_create(0, WIDTH, HEIGHT)
    context = cairo.cairo_create(surface)
    try:
        if not handle or not rsvg.rsvg_handle_render_cairo(handle, context):
            raise RuntimeError("Could not render terminal SVG")
        if png and cairo.cairo_surface_write_to_png(surface, str(png).encode()):
            raise RuntimeError("Could not save preview PNG")
        cairo.cairo_surface_flush(surface)
        stride = cairo.cairo_image_surface_get_stride(surface)
        pixels = C.string_at(cairo.cairo_image_surface_get_data(surface), stride * HEIGHT)
        indices = bytearray(WIDTH * HEIGHT)
        for y in range(HEIGHT):
            for x in range(WIDTH):
                p = y * stride + x * 4
                b, g, r, a = pixels[p:p + 4]
                if a < 255:  # Flatten rounded corners onto the terminal background.
                    r += round(int(BACKGROUND[1:3], 16) * (255 - a) / 255)
                    g += round(int(BACKGROUND[3:5], 16) * (255 - a) / 255)
                    b += round(int(BACKGROUND[5:7], 16) * (255 - a) / 255)
                rgb = (r, g, b)
                if rgb not in COLOR_CACHE:
                    COLOR_CACHE[rgb] = min(
                        range(128),
                        key=lambda i: sum((a - b) ** 2 for a, b in zip(rgb, PALETTE[i])),
                    )
                indices[y * WIDTH + x] = COLOR_CACHE[rgb]
        return indices
    finally:
        cairo.cairo_destroy(context)
        cairo.cairo_surface_destroy(surface)
        if handle:
            gobject.g_object_unref(handle)


def lzw(data):
    """GIF LZW with a full 12-bit dictionary for compact ASCII animations."""
    table = {bytes([i]): i for i in range(256)}
    next_code = 258
    codes = [256]
    prefix = b""
    for pixel in data:
        suffix = bytes([pixel])
        pair = prefix + suffix
        if pair in table:
            prefix = pair
            continue
        codes.append(table[prefix])
        if next_code < 4096:
            table[pair] = next_code
            next_code += 1
        else:
            codes.append(256)
            table = {bytes([i]): i for i in range(256)}
            next_code = 258
        prefix = suffix
    if prefix:
        codes.append(table[prefix])
    codes.append(257)
    encoded = bytearray()
    buffer = bits = 0
    code_width, decoder_next, has_previous = 9, 258, False
    for code in codes:
        buffer |= code << bits
        bits += code_width
        while bits >= 8:
            encoded.append(buffer & 255)
            buffer >>= 8
            bits -= 8
        # The decoder inserts its first dictionary entry after two data codes.
        # Track its width separately so boundaries and the end code align.
        if code == 256:
            code_width, decoder_next, has_previous = 9, 258, False
        elif code != 257:
            if has_previous:
                decoder_next += 1
                if decoder_next == 1 << code_width and code_width < 12:
                    code_width += 1
            has_previous = True
    if bits:
        encoded.append(buffer & 255)
    blocks = bytearray([8])
    for offset in range(0, len(encoded), 255):
        chunk = encoded[offset:offset + 255]
        blocks.append(len(chunk))
        blocks.extend(chunk)
    blocks.append(0)
    return blocks


def write_gif(frames, path):
    output = bytearray(b"GIF89a" + struct.pack("<HHBBB", WIDTH, HEIGHT, 0xF6, 0, 0))
    output.extend(bytes(channel for color in PALETTE for channel in color))
    output.extend(b"\x21\xff\x0bNETSCAPE2.0\x03\x01\x00\x00\x00")
    previous = None
    for pixels, delay in frames:
        x0, y0, x1, y1 = 0, 0, WIDTH - 1, HEIGHT - 1
        if previous is not None:
            changed = [i for i, value in enumerate(pixels) if value != previous[i]]
            if changed:
                x0 = min(i % WIDTH for i in changed)
                x1 = max(i % WIDTH for i in changed)
                y0, y1 = changed[0] // WIDTH, changed[-1] // WIDTH
            else:
                x0 = x1 = y0 = y1 = 0
        patch = bytearray()
        for y in range(y0, y1 + 1):
            patch.extend(pixels[y * WIDTH + x0:y * WIDTH + x1 + 1])
        output.extend(b"\x21\xf9\x04\x04" + struct.pack("<H", delay) + b"\x00\x00")
        output.extend(b"," + struct.pack("<HHHHB", x0, y0, x1 - x0 + 1, y1 - y0 + 1, 0))
        output.extend(lzw(patch))
        previous = pixels
    output.append(0x3B)
    path.write_bytes(output)


def main():
    outputs = capture_outputs()
    libraries = native_rendering()
    scenes, lines = [], []
    for command, output in zip(COMMANDS, outputs):
        row = len(lines)
        scenes.append((svg_frame(lines + [("", True)], row, 0), 65))
        for end in range(3, len(command) + 3, 3):
            typed = command[:end]
            scenes.append((svg_frame(lines + [(typed, True)], row, len(typed)), 12))
        scenes[-1] = (scenes[-1][0], 35)
        lines.extend([(command, True), (output, False)])
        scenes.append((svg_frame(lines), 60))
    final_svg = svg_frame(lines + [("", True)], 6, 0)
    scenes.append((final_svg, 280))
    ASSETS.joinpath("terminal-demo.svg").write_bytes(final_svg)
    frames = [(rasterize(svg, libraries), delay) for svg, delay in scenes]
    write_gif(frames, ASSETS / "terminal-demo.gif")
    for index, name in [(0, "start"), (6, "hello"), (-1, "final")]:
        rasterize(scenes[index][0], libraries, Path(f"/tmp/linux-lab-terminal-{name}.png"))
    print(f"Executed in {CWD.relative_to(ROOT)}")
    for command, output in zip(COMMANDS, outputs):
        print(f"$ {command}\n{output}")
    print(f"GIF: {len(frames)} frames, {sum(delay for _, delay in scenes) / 100:.2f}s, "
          f"{ASSETS.joinpath('terminal-demo.gif').stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
