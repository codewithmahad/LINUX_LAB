# Navigation and Paths

Practical notes from learning Linux filesystem navigation, paths, and basic directory listing commands.

---

## Command Structure

A Linux command commonly follows this structure:

```text
command [options] [arguments]
```

Example:

```bash
ls -la learning
```

- `ls` — command
- `-la` — options
- `learning` — argument

---

## `pwd` — Print Working Directory

Displays the absolute path of the current working directory.

```bash
pwd
```

Example:

```text
/home/mahad/Github-Repo-Clones/LINUX_LAB
```

---

## `ls` — List Directory Contents

List the contents of the current directory:

```bash
ls
```

Display one entry per line:

```bash
ls -1
```

Display detailed information:

```bash
ls -l
```

Include hidden files:

```bash
ls -a
```

Combine long format, human-readable sizes, and hidden files:

```bash
ls -lha
```

Options used:

- `-1` — one entry per line
- `-l` — long listing format
- `-a` — include hidden entries
- `-h` — human-readable file sizes

Single-letter options can often be combined.

---

## Absolute and Relative Paths

### Absolute Path

Starts from the filesystem root `/` and gives the complete location.

Example:

```text
/home/mahad/Github-Repo-Clones/LINUX_LAB
```

### Relative Path

Starts from the current working directory.

Example:

```text
learning/linux-commands
```

---

## Special Path Symbols

| Symbol | Meaning |
| --- | --- |
| `/` | Filesystem root |
| `~` | Current user's home directory |
| `.` | Current directory |
| `..` | Parent directory |

---

## `cd` — Change Directory

Move into a directory:

```bash
cd learning
```

Move one directory upward:

```bash
cd ..
```

Move two levels upward:

```bash
cd ../..
```

Move to the home directory:

```bash
cd ~
```

Return to the previous working directory:

```bash
cd -
```

---

## Tab Completion

Press `Tab` while typing a command or path to automatically complete it when possible.

Example:

```text
cd lea<Tab>
```

can expand to:

```text
cd learning/
```

Tab completion reduces typing and helps avoid path-name mistakes.