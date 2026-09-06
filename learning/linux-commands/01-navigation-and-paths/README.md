# Navigation and Paths

Linux command-line work starts with knowing **where you are, what is around you, and how to move through the filesystem**.

This section covers the basic commands and path concepts used for navigating a Linux system.

---

## Command Structure

Most Linux commands follow a general structure:

```text
command [options] [arguments]
```

Example:

```bash
ls -la learning
```

Here:

- `ls` is the command.
- `-la` contains options that change how the command behaves.
- `learning` is the argument, in this case the directory to list.

Options are commonly written using `-` followed by one or more letters.

---

## `pwd`: Print Working Directory

`pwd` displays the absolute path of the directory you are currently working in.

```bash
pwd
```

Example output:

```text
/home/mahad/Github-Repo-Clones/LINUX_LAB
```

This is useful whenever you want to confirm your current location in the filesystem.

---

## `ls`: List Directory Contents

`ls` displays the contents of a directory.

### Basic Listing

```bash
ls
```

Lists the visible files and directories in the current location.

### One Entry Per Line

```bash
ls -1
```

The `-1` option displays each entry on a separate line.

### Long Listing

```bash
ls -l
```

Displays additional information such as:

- file permissions,
- owner,
- group,
- size,
- modification time,
- file or directory name.

### Include Hidden Files

```bash
ls -a
```

The `-a` option includes hidden files and directories.

In Linux, names beginning with `.` are normally hidden.

Examples:

```text
.git
.gitignore
```

### Human-Readable Detailed Listing

```bash
ls -lha
```

This combines three options:

| Option | Meaning |
| --- | --- |
| `-l` | Long listing format |
| `-h` | Human-readable file sizes |
| `-a` | Include hidden entries |

For example, `4096` bytes may be displayed as `4.0K`.

Single-letter options can often be combined:

```bash
ls -l -h -a
```

and:

```bash
ls -lha
```

are equivalent.

---

## Absolute and Relative Paths

Linux commands frequently work with filesystem paths.

There are two important types.

### Absolute Path

An absolute path describes the complete location of a file or directory starting from the filesystem root `/`.

Example:

```text
/home/mahad/Github-Repo-Clones/LINUX_LAB
```

An absolute path works regardless of the current working directory.

Example:

```bash
cd /home/mahad/Github-Repo-Clones/LINUX_LAB
```

---

### Relative Path

A relative path is interpreted from the current working directory.

Example:

```text
learning/linux-commands
```

If the current directory is:

```text
/home/mahad/Github-Repo-Clones/LINUX_LAB
```

then:

```text
learning/linux-commands
```

refers to:

```text
/home/mahad/Github-Repo-Clones/LINUX_LAB/learning/linux-commands
```

Relative paths are usually shorter and more convenient when working inside a project.

---

## Important Path Symbols

| Symbol | Meaning |
| --- | --- |
| `/` | Root of the Linux filesystem |
| `~` | Current user's home directory |
| `.` | Current directory |
| `..` | Parent directory |

For the current user:

```text
~ = /home/mahad
```

The filesystem root `/` and the user's home directory `~` are different locations.

A simplified example:

```text
/
├── etc
├── home
│   └── mahad
├── tmp
└── usr
```

Here, `/home/mahad` exists inside the filesystem rooted at `/`.

---

## `cd`: Change Directory

`cd` is used to move between directories.

### Enter a Directory

```bash
cd learning
```

---

### Move to the Parent Directory

```bash
cd ..
```

`..` represents the parent of the current directory.

---

### Move Up Multiple Levels

```bash
cd ../..
```

Each `..` moves one level upward.

---

### Move to the Home Directory

```bash
cd ~
```

A shorter equivalent is simply:

```bash
cd
```

Both move to the current user's home directory.

---

### Return to the Previous Directory

```bash
cd -
```

This switches back to the previous working directory.

It is useful when repeatedly moving between two locations.

Example:

```bash
cd ~
cd -
```

---

## Current and Parent Directory Entries

Running:

```bash
ls -la
```

also shows:

```text
.
..
```

These have special meanings:

```text
.   current directory
..  parent directory
```

This is why a command such as:

```bash
code .
```

means:

> Open the current directory in Visual Studio Code.

---

## Tab Completion

Bash can automatically complete command names and filesystem paths.

Start typing a path:

```text
cd lea
```

then press `Tab`.

If there is a unique match, Bash may complete it to:

```text
cd learning/
```

Tab completion is useful because it:

- reduces typing,
- avoids spelling mistakes,
- makes long paths easier to work with.

If multiple matches exist, pressing `Tab` again may display the available possibilities.

---

## Useful Terminal Shortcuts

These shortcuts make command-line work faster.

| Shortcut | Purpose |
| --- | --- |
| `Tab` | Auto-complete commands and paths |
| `↑` / `↓` | Browse previously executed commands |
| `Ctrl + L` | Clear the visible terminal |
| `Ctrl + C` | Cancel the currently running command |
| `Ctrl + R` | Search backward through command history |

### Reverse History Search

Press:

```text
Ctrl + R
```

and start typing part of an earlier command.

For example:

```text
git push
```

Bash can search your command history for a previous matching command such as:

```bash
git push origin main
```

---

## Quick Reference

```bash
pwd                 # Show current directory

ls                  # List directory contents
ls -1               # One entry per line
ls -l               # Detailed listing
ls -a               # Include hidden files
ls -lha              # Detailed, human-readable, including hidden files

cd learning         # Enter a directory
cd ..               # Move one level up
cd ../..             # Move two levels up
cd ~                 # Go to home directory
cd                   # Also go to home directory
cd -                 # Return to previous directory

ls /                 # List the filesystem root
```

---

## Key Takeaways

- `pwd` tells you where you currently are.
- `ls` shows what exists in a directory.
- `cd` moves between directories.
- Absolute paths start from `/`.
- Relative paths depend on the current working directory.
- `~` represents the user's home directory.
- `.` represents the current directory.
- `..` represents the parent directory.
- Hidden Linux files usually begin with `.`.
- Tab completion and command-history shortcuts make terminal work much faster.
