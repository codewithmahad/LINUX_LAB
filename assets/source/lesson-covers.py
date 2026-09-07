#!/usr/bin/env python3
"""Build the lesson diagrams with the existing cover palette and original Tux.

Run from any directory: python3 assets/source/lesson-covers.py
Uses only the Python standard library. Tux is embedded unchanged; see assets/README.md.
These are explanatory layouts, not terminal screenshots.
"""

import base64
from html import escape
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1]
OUT = ASSETS / "lessons"
SANS = "Ubuntu, DejaVu Sans, Arial, sans-serif"
MONO = "Ubuntu Mono, DejaVu Sans Mono, monospace"
TUX = base64.b64encode((ASSETS / "tux.png").read_bytes()).decode("ascii")


def text(x, y, value, size=24, color="#172D42", weight=400, mono=False):
    return (f'<text x="{x}" y="{y}" font-family="{MONO if mono else SANS}" '
            f'font-size="{size}" font-weight="{weight}" fill="{color}">{escape(value)}</text>')


def rect(x, y, w, h, fill, radius=12, stroke=None):
    border = f' stroke="{stroke}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}"{border}/>'


def tux(x, y, height):
    width = round(height * 265 / 314, 2)
    return (f'<image x="{x}" y="{y}" width="{width}" height="{height}" '
            f'href="data:image/png;base64,{TUX}"/>')


def svg(w, h, title, description, parts):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="title description">\n'
            f'<title id="title">{escape(title)}</title>\n'
            f'<desc id="description">{escape(description)}</desc>\n'
            + "\n".join(parts) + "\n</svg>\n")


def folder(x, y, w, mobile=False):
    """One folder, two files. The names match chapter two's actual commands."""
    h = 205
    parts = [
        f'<path d="M{x} {y+18} Q{x} {y} {x+18} {y} H{x+135} '
        f'L{x+158} {y+23} H{x+w-18} Q{x+w} {y+23} {x+w} {y+41} '
        f'V{y+h-18} Q{x+w} {y+h} {x+w-18} {y+h} H{x+18} '
        f'Q{x} {y+h} {x} {y+h-18} Z" fill="#EDD8B7"/>',
        rect(x, y+36, w, h-36, "#F3E5D0", 16),
        text(x+24, y+69, "notes/", 26, "#59452C", 500, True),
    ]
    for offset, name in [(85, "today.txt"), (140, "questions.txt")]:
        parts += [
            rect(x+24, y+offset, w-48, 46, "#FFFDF8", 8),
            f'<path d="M{x+43} {y+offset+11} h12 l6 6 v18 h-18 Z '
            f'M{x+55} {y+offset+11} v6 h6" fill="none" stroke="#876F4F" '
            'stroke-width="1.8" stroke-linejoin="round"/>',
            text(x+79, y+offset+31, name, 23, "#59452C", mono=True),
            text(x+w-105, y+offset+29, "0 bytes", 16, "#75674F", mono=True),
        ]
    return parts


def files_cover(mobile=False):
    w, h = (640, 420) if mobile else (1120, 340)
    parts = [rect(0, 0, w, h, "#F7F5EE", 18)]
    if mobile:
        parts += [text(28, 35, "LINUX_LAB / 02", 17, "#526172", 500),
                  text(28, 88, "Make room for", 37, weight=600),
                  text(28, 132, "your ideas.", 37, "#2475B7", 600),
                  tux(521, 34, 106),
                  text(38, 184, "mkdir notes", 23, "#2475B7", mono=True)]
        parts += folder(38, 197, 564, True)
    else:
        parts += [rect(556, 18, 546, 304, "#E2EDF6", 14),
                  text(40, 47, "LINUX_LAB / 02", 18, "#526172", 500),
                  text(40, 112, "Make room for", 46, weight=600),
                  text(40, 167, "your ideas.", 46, "#2475B7", 600),
                  text(41, 207, "A folder. A few files. A place to start.", 22, "#526172"),
                  tux(42, 230, 85),
                  text(133, 265, "SHAIKH MAHAD", 17, "#172D42", 500),
                  text(133, 293, "Learning Linux, one command at a time.", 17, "#526172"),
                  text(590, 54, "mkdir notes", 23, "#2475B7", mono=True)]
        parts += folder(590, 69, 478)
        parts += [text(612, 304, "touch creates the empty files", 21, "#41647E")]
    return svg(w, h, "Make room for your ideas. Files and Directories.",
               "mkdir notes creates a folder. touch notes/today.txt notes/questions.txt "
               "creates two empty files inside it. Original Tux by Larry Ewing, created using The GIMP.", parts)


def selections(x, y, mobile=False):
    """Two coloured ranges from the bundled 12-line sample, with six lines omitted."""
    box_x = x + 165
    box_w = 367 if mobile else 337
    parts = []
    groups = [
        (0, "head -n 3", "#9CDCFE", "#19354B", [("01", "Session started"),
          ("02", "Opened the Linux terminal"), ("03", "Checked location with pwd")]),
        (146, "tail -n 3", "#A9D6B7", "#193B35", [("10", "Retried the backup"),
          ("11", "Backup completed"), ("12", "Session finished")]),
    ]
    for offset, command, accent, fill, rows in groups:
        yy = y + offset
        parts += [rect(box_x, yy, box_w, 110, fill, 10),
                  text(x, yy+49, command, 22, accent, mono=True),
                  text(x, yy+76, "first 3 lines" if not offset else "last 3 lines", 17, "#B1BFCD")]
        for i, (number, content) in enumerate(rows):
            baseline = yy + 28 + i*32
            parts += [text(box_x+14, baseline, number, 17, accent, mono=True),
                      text(box_x+49, baseline, content, 17, "#E6EDF3", mono=True)]
    parts += [text(box_x+49, y+133, "6 lines in between", 17, "#91A3B6", mono=True)]
    return parts


def reading_cover(mobile=False):
    w, h = (640, 444) if mobile else (1120, 340)
    parts = [rect(0, 0, w, h, "#101C2A", 18)]
    if mobile:
        parts += [text(28, 35, "LINUX_LAB / 03", 17, "#B1BFCD", 500),
                  text(28, 88, "Read a little.", 37, "#F7F5EE", 600),
                  text(28, 132, "Find a lot.", 37, "#9CDCFE", 600),
                  tux(521, 34, 106)]
        parts += selections(36, 163, True)
    else:
        parts += [text(40, 47, "LINUX_LAB / 03", 18, "#B1BFCD", 500),
                  text(40, 112, "Read a little.", 46, "#F7F5EE", 600),
                  text(40, 167, "Find a lot.", 46, "#9CDCFE", 600),
                  text(41, 207, "Same file. Two different views.", 22, "#B1BFCD"),
                  tux(42, 230, 85),
                  text(133, 265, "SHAIKH MAHAD", 17, "#F7F5EE", 500),
                  text(133, 293, "There's usually a clue in the log.", 17, "#B1BFCD"),
                  text(573, 44, "session.txt / 12 lines / excerpts", 18, "#B1BFCD", mono=True)]
        parts += selections(573, 62)
    return svg(w, h, "Read a little. Find a lot. Viewing File Content.",
               "The 12-line examples/session.txt: head -n 3 selects lines 1, 2, 3; "
               "tail -n 3 selects lines 10, 11, 12. These excerpts omit the log timestamps "
               "and levels. Original Tux by Larry Ewing, created using The GIMP.", parts)


def file_operations(x, y, width):
    """Two path changes, using the actual note and backup names from chapter four."""
    half = (width - 52) / 2
    parts = []
    for offset, command, meaning, first, last, fill, accent in [
        (0, "cp", "source + copy", "notes.txt", "notes-backup.txt", "#2B2E43", "#C0CEF4"),
        (142, "mv", "old path to new path", "notes-backup.txt", "notes-final.txt", "#3C2C30", "#ECC68B"),
    ]:
        yy = y + offset
        parts += [text(x, yy, command, 25, accent, 600, True),
                  text(x+57, yy, meaning, 19, "#D0C4D1"),
                  rect(x, yy+20, half, 58, fill, 8),
                  rect(x+half+52, yy+20, half, 58, fill, 8),
                  text(x+14, yy+56, first, 19, accent, mono=True),
                  text(x+half+66, yy+56, last, 19, accent, mono=True)]
        if command == "cp":
            parts += [text(x+half+16, yy+56, "+", 24, accent, mono=True),
                      text(x+14, yy+106, "original stays", 17, "#B8AABA"),
                      text(x+half+66, yy+106, "copy added", 17, "#B8AABA")]
        else:
            parts += [f'<path d="M{x+half+10} {yy+49} h29 l-7 -7 m7 7 l-7 7" '
                      f'fill="none" stroke="{accent}" stroke-width="2" stroke-linecap="round"/>',
                      text(x+14, yy+106, "old name gone", 17, "#B8AABA"),
                      text(x+half+66, yy+106, "new name kept", 17, "#B8AABA")]
    return parts


def copying_cover(mobile=False):
    w, h = (640, 464) if mobile else (1120, 340)
    parts = [rect(0, 0, w, h, "#241B2A", 18)]
    if mobile:
        parts += [text(28, 35, "LINUX_LAB / 04", 17, "#C3B5C7", 500),
                  text(28, 88, "Keep a copy.", 37, "#F7F5EE", 600),
                  text(28, 132, "Move with care.", 37, "#ECC68B", 600),
                  tux(521, 34, 106)]
        parts += file_operations(32, 188, 576)
    else:
        parts += [text(40, 47, "LINUX_LAB / 04", 18, "#C3B5C7", 500),
                  text(40, 112, "Keep a copy.", 46, "#F7F5EE", 600),
                  text(40, 167, "Move with care.", 46, "#ECC68B", 600),
                  text(41, 207, "Check where each file ends up.", 22, "#C3B5C7"),
                  tux(42, 230, 85),
                  text(133, 265, "SHAIKH MAHAD", 17, "#F7F5EE", 500),
                  text(133, 293, "A little organisation goes a long way.", 17, "#C3B5C7")]
        parts += file_operations(570, 53, 510)
    return svg(w, h, "Keep a copy. Move with care. Copying, Moving, and Deleting.",
               "cp project/notes.txt notes-backup.txt keeps the original and creates a copy. "
               "Later, mv archive/notes-backup.txt archive/notes-final.txt renames that copy. "
               "The diagram omits directory prefixes. Original Tux by Larry Ewing, created using The GIMP.", parts)


def search_document(x, y, width):
    """A located path and the two selected lines from chapter five's sample."""
    return [
        text(x, y, "01 / FIND THE FILE", 17, "#A4492B", 600),
        rect(x, y+18, width, 57, "#F2E5D4", 8),
        text(x+18, y+53, "workspace/logs/session.txt", 22, "#513E32", mono=True),
        f'<path d="M{x+25} {y+86} v23 l-6 -6 m6 6 l6 -6" '
        'fill="none" stroke="#A4492B" stroke-width="2" stroke-linecap="round"/>',
        text(x+48, y+108, "02 / SEARCH INSIDE", 17, "#A4492B", 600),
        rect(x, y+127, width, 114, "#FFFDF8", 10, "#E4D9CA"),
        text(x+18, y+161, "grep -n 'ERROR'", 20, "#513E32", mono=True),
        rect(x+15, y+176, 39, 50, "#F8DFCE", 5),
        text(x+22, y+196, "4", 17, "#A4492B", 600, True),
        text(x+65, y+196, "Could not save notes.txt", 17, "#513E32", mono=True),
        text(x+22, y+219, "7", 17, "#A4492B", 600, True),
        text(x+65, y+219, "Permission denied for archive.txt", 17, "#513E32", mono=True),
    ]


def searching_cover(mobile=False):
    w, h = (640, 444) if mobile else (1120, 340)
    parts = [rect(0, 0, w, h, "#F7F5EE", 18)]
    if mobile:
        parts += [text(28, 35, "LINUX_LAB / 05", 17, "#6F655C", 500),
                  text(28, 88, "Where is it?", 37, "#382C31", 600),
                  text(28, 132, "What's inside?", 37, "#A4492B", 600),
                  tux(521, 34, 106)]
        parts += search_document(32, 178, 576)
    else:
        parts += [text(40, 47, "LINUX_LAB / 05", 18, "#6F655C", 500),
                  text(40, 112, "Where is it?", 46, "#382C31", 600),
                  text(40, 167, "What's inside?", 46, "#A4492B", 600),
                  text(41, 207, "A path first. The right lines next.", 22, "#6F655C"),
                  tux(42, 230, 85),
                  text(133, 265, "SHAIKH MAHAD", 17, "#382C31", 500),
                  text(133, 293, "Let the terminal do the looking.", 17, "#6F655C")]
        parts += search_document(564, 44, 520)
        parts += [text(580, 310, "line numbers kept / timestamps omitted", 16, "#6F655C", mono=True)]
    return svg(w, h, "Where is it? What's inside? Searching and Finding.",
               "find locates examples/workspace/logs/session.txt. grep -n 'ERROR' selects "
               "line 4, Could not save notes.txt, and line 7, Permission denied for archive.txt. "
               "The diagram shortens the path and omits timestamps and ERROR prefixes. "
               "Original Tux by Larry Ewing, created using The GIMP.", parts)


def label_counts(x, y, width):
    """Six actual input labels and their frequencies after sort and uniq -c."""
    parts = [text(x, y, "labels.txt", 20, "#CFDACF", mono=True),
             text(x+224, y, "count / label", 20, "#CFDACF", mono=True)]
    for i, label in enumerate(["bash", "linux", "linux", "git", "bash", "linux"]):
        parts.append(text(x+6, y+39+i*29, label, 22, "#F7F5EE", mono=True))
    parts += [f'<path d="M{x+121} {y+110} h62 l-8 -8 m8 8 l-8 8" '
              'fill="none" stroke="#D7AD6C" stroke-width="2.5" stroke-linecap="round"/>']
    for i, (label, count) in enumerate([("bash", 2), ("git", 1), ("linux", 3)]):
        yy = y+21+i*59
        parts += [rect(x+217, yy, width-217, 47, "#1D3733", 7),
                  rect(x+217, yy+42, (width-217)*count/3, 5, "#A9D6B7", 2),
                  text(x+233, yy+31, str(count), 24, "#D7AD6C", 500, True),
                  text(x+279, yy+31, label, 24, "#F7F5EE", mono=True)]
    parts += [text(x, y+234, "sort labels.txt | uniq -c", 22, "#A9D6B7", mono=True)]
    return parts


def processing_cover(mobile=False):
    w, h = (640, 444) if mobile else (1120, 340)
    parts = [rect(0, 0, w, h, "#112622", 18)]
    if mobile:
        parts += [text(28, 35, "LINUX_LAB / 06", 17, "#AFBCB5", 500),
                  text(28, 88, "A few lines.", 37, "#F7F5EE", 600),
                  text(28, 132, "A useful answer.", 37, "#A9D6B7", 600),
                  tux(521, 34, 106)]
        parts += label_counts(36, 183, 568)
    else:
        parts += [text(40, 47, "LINUX_LAB / 06", 18, "#AFBCB5", 500),
                  text(40, 112, "A few lines.", 46, "#F7F5EE", 600),
                  text(40, 167, "A useful answer.", 46, "#A9D6B7", 600),
                  text(41, 207, "Count. Sort. Pick out what matters.", 22, "#AFBCB5"),
                  tux(42, 230, 85),
                  text(133, 265, "SHAIKH MAHAD", 17, "#F7F5EE", 500),
                  text(133, 293, "Six entries. Three labels. That's useful.", 17, "#AFBCB5")]
        parts += label_counts(582, 60, 498)
    return svg(w, h, "A few lines. A useful answer. Text Processing.",
               "examples/labels.txt contains bash, linux, linux, git, bash, linux in that order. "
               "sort followed by uniq -c groups and counts them: 2 bash, 1 git, 3 linux. "
               "The bars represent those counts. Original Tux by Larry Ewing, created using The GIMP.", parts)


def main():
    OUT.mkdir(exist_ok=True)
    for name, build in [("files-and-directories", files_cover),
                        ("viewing-file-content", reading_cover),
                        ("copying-moving-and-deleting", copying_cover),
                        ("searching-and-finding", searching_cover),
                        ("text-processing", processing_cover)]:
        for mobile in (False, True):
            suffix = "-mobile" if mobile else ""
            path = OUT / f"{name}{suffix}.svg"
            path.write_text(build(mobile), encoding="utf-8")
            print(path.relative_to(ASSETS.parent))


if __name__ == "__main__":
    main()
