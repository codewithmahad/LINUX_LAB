# Artwork and sources

The main README pairs the original Tux with a small title. The filesystem, DeployLatch, and Ubuntu artwork sit alongside their sections; the Bash mark appears inside its fundamentals dropdown. This page records their sources and the chapter illustration credits.

## README artwork

| Artwork | Files | Source |
| :--- | :--- | :--- |
| Title | [Light](readme/linux-title-light.svg) · [Dark](readme/linux-title-dark.svg) | Text-only wordmark drawn for this repository, in charcoal and silver. |
| Linux filesystem | [Light](readme/filesystem-light.svg) · [Dark](readme/filesystem-dark.svg) | Original sketch of selected directories under `/`: `home`, `var`, and `opt`. |
| Bash | [Light](readme/bash-light.svg) · [Dark](readme/bash-dark.svg) | Grayscale presentations of the GNU Bash logo; attribution and terms below. |
| DeployLatch | [Light](readme/deploylatch-light.svg) · [Dark](readme/deploylatch-dark.svg) | Existing project emblems, copied unchanged from my DeployLatch repository. |
| Tux | [Original PNG](tux.png) | Larry Ewing's Linux penguin, displayed unchanged beside the introduction. [Credit and source](#tux). |
| Ubuntu | [Original SVG](logos/ubuntu.svg) | Canonical's Circle of Friends, displayed unchanged beside the setup section. [Credit and terms](#project-logos). |

The title and filesystem sketches are directly editable SVGs using system fonts. Those original layouts use the repository's [MIT license](../LICENSE). The logos retain their own attribution and terms.

### Grayscale Bash marks

The GNU Bash logo was designed by **Prospect One**, copyright **2016 Free Software Foundation**, under the [Free Art License 1.3](https://artlibre.org/licence/lal/en/).

The README's two grayscale presentations come from the [original light-background](logos/bash.svg) and [original dark-background](logos/bash-dark.svg) versions already stored here. Only the colors were changed to gray, charcoal, and silver; the logo geometry is unchanged. These presentations retain the original attribution and Free Art License.

Original sources: [official logo project](https://github.com/odb/official-bash-logo) · [designer's downloads](https://bashlogo.com/).

### DeployLatch emblem

The [light](readme/deploylatch-light.svg) and [dark](readme/deploylatch-dark.svg) emblems are copied unchanged from [DeployLatch's light mark](https://github.com/codewithmahad/deploylatch/blob/main/docs/assets/deploylatch-mark.svg) and [dark mark](https://github.com/codewithmahad/deploylatch/blob/main/docs/assets/deploylatch-mark-on-dark.svg). They are project-authored vector adaptations of my supplied logo, with its lock, server, upload arrow, and recovery arrows. The project records their origin in its [artwork notes](https://github.com/codewithmahad/deploylatch/blob/main/docs/assets/THIRD_PARTY.md).

## Lesson covers

The Linux command chapters use explanatory covers with a palette chosen for each topic. Chapter 07 pairs dark cherry with amber and rose to separate output streams; chapter 08 uses pale pistachio and green to break down permission modes. The Bash covers use aubergine, peach, and green. Each has a compact version for narrow screens. The original Tux, Bash, and Ubuntu artwork are embedded unchanged, with [Larry Ewing's credit](#tux) and the [project logo credits](#project-logos).

| Chapter | Wide cover | Compact cover | What the diagram shows |
| :--- | :--- | :--- | :--- |
| Files and Directories | [SVG](lessons/files-and-directories.svg) | [SVG](lessons/files-and-directories-mobile.svg) | A `notes` folder containing two empty files, matching the chapter's commands. |
| Viewing File Content | [SVG](lessons/viewing-file-content.svg) | [SVG](lessons/viewing-file-content-mobile.svg) | The first and last three lines of the supplied 12-line session. Excerpts omit timestamps and log levels for space. |
| Copying, Moving, and Deleting | [SVG](lessons/copying-moving-and-deleting.svg) | [SVG](lessons/copying-moving-and-deleting-mobile.svg) | Copying keeps the original note and adds a backup; moving renames the backup. Directory prefixes are omitted for space. |
| Searching and Finding | [SVG](lessons/searching-and-finding.svg) | [SVG](lessons/searching-and-finding-mobile.svg) | Finding a file, then selecting its two error lines. The path is shortened; timestamps and log levels are omitted. |
| Text Processing | [SVG](lessons/text-processing.svg) | [SVG](lessons/text-processing-mobile.svg) | The six supplied labels become three frequency counts. Bar lengths show the counts. |
| Redirection and Pipes | [SVG](lessons/redirection-and-pipes.svg) | [SVG](lessons/redirection-and-pipes-mobile.svg) | `cat` sends the note's contents and a missing-file diagnostic through separate stdout and stderr routes to two files. |
| Permissions and Ownership | [SVG](lessons/permissions-and-ownership.svg) | [SVG](lessons/permissions-and-ownership-mobile.svg) | The actual `chmod 640 note.txt` example: owner read/write, group read, and no access for others. |
| Bash 01: Shell and Script Basics | [SVG](lessons/bash-shell-and-script-basics.svg) | [SVG](lessons/bash-shell-and-script-basics-mobile.svg) | The complete `hello.sh` source, the command that runs it, and its actual greeting. |
| Bash 02: Variables and Expansion | [SVG](lessons/bash-variables-and-expansion.svg) | [SVG](lessons/bash-variables-and-expansion-mobile.svg) | The two greetings from `quoting.sh`, showing expansion inside double quotes and literal text inside single quotes. |
| Bash 03: Input and Output | [SVG](lessons/bash-input-and-output.svg) | [SVG](lessons/bash-input-and-output-mobile.svg) | One answer travels from `read` through a variable to `printf`. The course prompt and summary heading from `input.sh` are omitted. |
| Bash 04: Operators and Expressions | [SVG](lessons/bash-operators-and-expressions.svg) | [SVG](lessons/bash-operators-and-expressions-mobile.svg) | Integer division produces the value `3`; a true arithmetic comparison leaves exit status `0`. |

These are diagrams, not terminal screenshots. Their meaning is also explained in the lessons and image descriptions. The layout code uses the repository's MIT license; the third-party artwork retains its original terms.

To rebuild the covers, using Python's standard library:

```bash
python3 assets/source/lesson-covers.py
```

The [source](source/lesson-covers.py) keeps the colours, labels, and layouts together. It reads the existing Tux image, Bash logo, and Ubuntu logo locally and needs no downloads or image-generation service.

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

The PNG is unmodified, including where it is embedded in the cover SVGs. Its original reuse terms and creator credit apply.
