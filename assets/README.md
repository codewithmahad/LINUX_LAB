# Artwork and terminal demos

The README uses local images, established project logos, and a terminal Easter egg. The source files and credits are kept here so the page can be maintained alongside the notes.

## Cover and journey

| Asset | Purpose |
| :--- | :--- |
| [linux-lab-hero.svg](linux-lab-hero.svg) | Wide cover with classic Tux and a dark terminal. |
| [linux-lab-hero-mobile.svg](linux-lab-hero-mobile.svg) | Compact cover for narrow screens. |
| [linux-lab-journey.svg](linux-lab-journey.svg) | The purple learning route, with current and future topics. |
| [linux-lab-closing.svg](linux-lab-closing.svg) | Dark closing banner and Shaikh Mahad's signature. |

The covers and closing banner embed the original Tux PNG. These are layouts built for the repository, not screenshots of a personal desktop. The SVG text and geometry are editable; the embedded Tux artwork retains its creator credit and original terms.

The repository-specific layout code uses the [MIT license](../LICENSE). The third-party artwork and logos below retain their own terms.

## Project logos

Downloaded logos are stored unmodified. Their presence identifies the tools discussed in the notes.

| Local file | Creator and original source | Terms |
| :--- | :--- | :--- |
| [ubuntu.svg](logos/ubuntu.svg) | Canonical Ltd., [official Circle of Friends SVG](https://assets.ubuntu.com/v1/ce518a18-CoF-2022_solid+O.svg) from [Ubuntu design resources](https://design.ubuntu.com/resources). | Ubuntu and the Circle of Friends are Canonical trademarks. See [Canonical's usage policy](https://canonical.com/legal/intellectual-property-policy). |
| [bash.svg](logos/bash.svg), [bash-dark.svg](logos/bash-dark.svg) | Designed by Prospect One, copyright 2016 Free Software Foundation. [Original logo project](https://github.com/odb/official-bash-logo), [designer's downloads](https://bashlogo.com/). | [Free Art License 1.3](https://artlibre.org/licence/lal/en/). The two official variants suit light and dark backgrounds. |
| [git.svg](logos/git.svg) | Jason Long, [official Git logo downloads](https://git-scm.com/community/logos). [Original SVG](https://git-scm.com/images/logos/downloads/Git-Icon-1788C.svg). | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). |
| [vscode.svg](logos/vscode.svg) | Microsoft Corporation. Extracted from the [official icon archive](https://code.visualstudio.com/assets/branding/visual-studio-code-icons.zip). | Microsoft retains its trademark rights. The [brand guidelines](https://code.visualstudio.com/brand) cover use in documentation and tutorials. |

The Bash source files are [the dark-outline variant](https://bashlogo.com/img/symbol/svg/full_colored_dark.svg) and [the light-outline variant](https://bashlogo.com/img/symbol/svg/full_colored_light.svg), respectively.

## Tux

[tux.png](tux.png) is **Tux, by Larry Ewing, created using The GIMP**.

- [Larry Ewing's original Linux artwork page](http://isc.tamu.edu/~lewing/linux/)
- [Wikimedia Commons source and reuse information](https://commons.wikimedia.org/wiki/File:Tux.png)
- [Downloaded PNG](https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png)
- [The Linux Kernel Archives' Tux attribution](https://origin.kernel.org/faq.html)

The PNG is unmodified, including where it is embedded in the cover and closing SVGs. Its original reuse terms and creator credit apply.

## Illustrated avatar

[shaikh-mahad-avatar.png](shaikh-mahad-avatar.png) uses the hooded character illustration supplied for this README. The built-in imagegen tool was used to create a transparent cutout, replacing the real profile photograph. This supplied artwork is separate from the repository's MIT-licensed code.

The [edit instructions](source/avatar-edit.md) record the requested transformation and tool used.

## Terminal Easter egg

[terminal-playground.gif](terminal-playground.gif) loops actual `sl` character output followed by `cowsay "mahad is dumb"`. [terminal-playground.svg](terminal-playground.svg) is the static version used for reduced motion. It is a styled replay of captured output with illustrative typing and timing.

The [renderer](source/terminal-playground.py) captures the train in a temporary tmux session and reads the cow's output. It does not access an existing tmux session.

Credits:

- **sl**, by Toyoda Masashi. Copyright 1993, 1998, 2014. [Original project and permission notice](https://github.com/mtoyoda/sl). The permission notice is retained in the renderer source.
- **cowsay**, by Tony Monroe. Copyright 1999-2000. [Original project](https://github.com/tnalpgge/rank-amateur-cowsay), [license copy](licenses/cowsay-LICENSE.txt). The renderer invokes the program; its program code is not bundled here.

To rebuild the Easter egg on Ubuntu:

```bash
sudo apt install sl cowsay tmux librsvg2-2 libcairo2 fonts-dejavu-core
python3 assets/source/terminal-playground.py
```

These are asset-maintenance commands. Readers do not need these packages for the lessons.

## Command replay source

[terminal-demo.py](source/terminal-demo.py) contains the shared SVG and GIF rendering utilities. It can also regenerate [terminal-demo.gif](terminal-demo.gif) and [terminal-demo.svg](terminal-demo.svg), which show the existing `hello.sh` example, remainder arithmetic, and an exit status.

```bash
python3 assets/source/terminal-demo.py
```

This uses Python 3, Bash, native librsvg and Cairo, and DejaVu fonts on Linux. It needs no Python packages or network access. The main README uses the train-and-cow Easter egg.
