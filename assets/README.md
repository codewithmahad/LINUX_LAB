# README artwork

The main README uses local images so its artwork does not depend on a badge or image-generation service.

## Linux Lab illustrations

These SVGs form the repository's own visual set: aubergine backgrounds, orange terminal prompts, warm cream lettering, and a penguin at the keyboard.

| Asset | Use |
| :--- | :--- |
| [linux-lab-hero.svg](linux-lab-hero.svg) | Wide opening illustration. |
| [linux-lab-hero-mobile.svg](linux-lab-hero-mobile.svg) | Compact opening illustration for narrow screens. |
| [linux-lab-journey.svg](linux-lab-journey.svg) | The learning route, with current and future stages labelled. |
| [linux-lab-mark.svg](linux-lab-mark.svg) | An original penguin and terminal illustration. |
| [linux-lab-workbench.svg](linux-lab-workbench.svg) | Closing illustration and personal signature. |

These are illustrations, not screenshots of a personal desktop. The custom penguin is distinct from the original Tux artwork credited below. The SVG source is editable, contains its own accessibility description, and uses local system fonts with fallbacks. These original assets use the repository's [MIT license](../LICENSE).

When updating progress, change the root README's counts and current chapter as well as any affected labels in the journey artwork. Keep future topics visibly marked as plans.

## Terminal demo

[terminal-demo.gif](terminal-demo.gif) replays commands whose output was captured from Bash. It is a rendered animation, rather than a screen recording. [terminal-demo.svg](terminal-demo.svg) provides the static version used for readers who prefer reduced motion.

The first command runs the existing [hello.sh](../learning/bash-scripting/01-shell-and-script-basics/hello.sh) from its chapter directory. The other commands demonstrate remainder arithmetic and an exit status. The copyable commands and explanations remain in the main README.

To rebuild both versions from the repository root:

```bash
python3 assets/source/terminal-demo.py
```

The [renderer source](source/terminal-demo.py) uses Python 3, Bash, the native librsvg and Cairo libraries, and DejaVu fonts on Linux. It needs no Python packages or network access. These tools are only needed to rebuild the animation; readers can use the lessons without them.

## Tux credit

[tux.png](tux.png) is **Tux, by Larry Ewing, created using The GIMP**. This is third-party artwork, separate from the original illustrations above.

- [Larry Ewing's original Linux artwork page](http://isc.tamu.edu/~lewing/linux/)
- [Wikimedia Commons source and reuse information](https://commons.wikimedia.org/wiki/File:Tux.png)
- [Downloaded PNG](https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png)
- [The Linux Kernel Archives' Tux attribution](https://origin.kernel.org/faq.html)

The PNG is stored unmodified. Its original reuse terms and creator credit apply.
