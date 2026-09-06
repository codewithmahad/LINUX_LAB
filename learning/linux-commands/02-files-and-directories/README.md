[Previous: Navigation and Paths](../01-navigation-and-paths/README.md) · [LINUX_LAB](../../../README.md) · [Learning map](../../../README.md#what-im-learning)

# Files and Directories

Linux work revolves around files and directories. This section covers the commands used to create them, inspect their type and metadata, and view directory structures from the terminal.

---

## `mkdir`: Create Directories

`mkdir` stands for **make directory**.

### Create a Directory

```bash
mkdir sandbox
```

Verify it:

```bash
ls
```

Example output:

```text
sandbox
```

---

### Create Multiple Directories

`mkdir` can accept more than one directory name:

```bash
mkdir documents images scripts
```

This creates all three directories with one command.

Equivalent to:

```bash
mkdir documents
mkdir images
mkdir scripts
```

---

## `mkdir -p`: Create Parent Directories

The `-p` option means **parents**.

It creates missing parent directories automatically.

```bash
mkdir -p projects/backend/spring
```

This can create the complete hierarchy:

```text
projects/
└── backend/
    └── spring/
```

Without `-p`, `mkdir` fails if an intermediate parent directory does not already exist.

Another useful property of `-p` is that it does not report an error if the requested directory already exists.

---

## Useful `mkdir` Options

| Option | Purpose |
| --- | --- |
| `-p` | Create missing parent directories |
| `-v` | Display each directory as it is created |

Example:

```bash
mkdir -pv projects/backend/spring
```

Possible output:

```text
mkdir: created directory 'projects'
mkdir: created directory 'projects/backend'
mkdir: created directory 'projects/backend/spring'
```

Single-letter options can be combined, so:

```bash
mkdir -p -v projects/backend/spring
```

and:

```bash
mkdir -pv projects/backend/spring
```

perform the same operation.

---

# `touch`: Create or Update Files

A common use of `touch` is creating an empty file.

```bash
touch notes.txt
```

Verify:

```bash
ls -l notes.txt
```

Example output:

```text
-rw-r--r-- 1 mahad mahad 0 Sep  5 15:40 notes.txt
```

The `0` indicates that the file currently contains zero bytes.

---

## Create Multiple Files

Like `mkdir`, `touch` accepts multiple arguments.

```bash
touch file1.txt file2.txt file3.txt
```

This creates all three files if they do not already exist.

---

## What `touch` Actually Does

`touch` is not fundamentally only a file-creation command.

Its main purpose is to **update file timestamps**.

If the file does not exist:

```bash
touch notes.txt
```

an empty file is created.

If the file already exists:

```bash
touch notes.txt
```

its timestamps are updated without deleting or changing its contents.

---

## Useful `touch` Options

### `-a`: Update Access Time Only

```bash
touch -a notes.txt
```

Updates the file's **access time** without changing its modification time.

---

### `-m`: Update Modification Time Only

```bash
touch -m notes.txt
```

Updates only the **modification time**.

---

### `-c`: Do Not Create a Missing File

Normally:

```bash
touch missing.txt
```

creates the file if it does not exist.

Using:

```bash
touch -c missing.txt
```

updates the timestamps only if the file already exists.

If it does not exist, no new file is created.

---

### `-t`: Set a Specific Timestamp

A timestamp can also be supplied manually.

Example:

```bash
touch -t 202609051500 notes.txt
```

The timestamp format is generally:

```text
[[CC]YY]MMDDhhmm[.ss]
```

This is less common during everyday development, but useful when timestamp control is required.

---

# `file`: Identify File Type

The `file` command examines a filesystem object and reports what kind of data it contains.

```bash
file sandbox/notes.txt
```

Example output from the terminal:

```text
sandbox/notes.txt: empty
```

For a directory:

```bash
file sandbox
```

Example:

```text
sandbox: directory
```

---

## File Extensions Are Not Everything in Linux

Linux does not rely entirely on filename extensions to determine file type.

A filename such as:

```text
something.txt
```

does not guarantee that the contents are actually plain text.

The `file` command examines the object rather than simply trusting its extension.

This makes it useful when working with unfamiliar files.

---

# `stat`: View Detailed File Metadata

`stat` displays detailed information about a file or directory.

```bash
stat sandbox/notes.txt
```

Example from the actual terminal:

```text
  File: sandbox/notes.txt
  Size: 0               Blocks: 0          IO Block: 4096   regular empty file
Device: 8,48    Inode: 48961       Links: 1
Access: (0644/-rw-r--r--)  Uid: ( 1000/   mahad)   Gid: ( 1000/   mahad)
Access: 2026-09-05 15:40:24.255938107 +0500
Modify: 2026-09-05 15:40:24.255938107 +0500
Change: 2026-09-05 15:40:24.255938107 +0500
Birth: 2026-09-05 15:40:24.255938107 +0500
```

Values such as the inode number and timestamps depend on the system and file.

---

## Important Information Shown by `stat`

`stat` can display:

- file name,
- file size,
- file type,
- inode number,
- number of links,
- permissions,
- user ID and owner,
- group ID and group,
- access time,
- modification time,
- metadata-change time,
- creation/birth time where supported.

Some of these concepts, especially permissions and inodes, are explored in more detail in later topics.

For quick inspection:

```bash
ls -l file
```

is usually enough.

For detailed filesystem metadata:

```bash
stat file
```

is more useful.

---

# File Timestamps

The `stat` output introduces several different timestamps.

### Access Time

```text
Access
```

Represents when the file's data was last accessed, depending on filesystem and mount behavior.

### Modification Time

```text
Modify
```

Represents when the **file contents** were last modified.

### Change Time

```text
Change
```

Represents when filesystem metadata associated with the file was last changed.

For example, changing permissions can update this value even when the file contents remain unchanged.

### Birth Time

```text
Birth
```

Represents the creation time of the file when the filesystem supports it.

---

# `tree`: Display Directory Structure

`tree` displays files and directories hierarchically.

```bash
tree
```

Example:

```text
.
├── documents
│   ├── file1.txt
│   └── file2.txt
├── images
├── notes.txt
└── scripts

3 directories, 3 files
```

This is often easier to understand than a flat `ls` listing when inspecting a project with several nested directories.

---

## Display a Specific Directory

Provide the directory as an argument:

```bash
tree sandbox
```

Example:

```text
sandbox
├── documents
│   ├── file1.txt
│   └── file2.txt
├── images
├── notes.txt
├── projects
│   └── backend
│       └── spring
└── scripts

7 directories, 3 files
```

---

## `tree -d`: Directories Only

The `-d` option tells `tree` to display only directories.

```bash
tree -d
```

Example:

```text
.
├── assets
├── automation
│   ├── backups
│   ├── developer-tools
│   ├── file-management
│   ├── log-processing
│   └── system-utilities
├── learning
│   ├── bash-scripting
│   └── linux-commands
├── practice
│   ├── bash-scripting
│   └── linux-commands
└── resources
    ├── references
    ├── roadmaps
    └── university-lab
```

Here:

```text
-d = directories only
```

---

## Display Another Location with `tree`

The path supplied to `tree` does not have to be the current directory.

For example:

```bash
tree ~
```

means:

> Display the directory tree starting from the current user's home directory.

Since:

```text
~ = /home/mahad
```

the command begins displaying the hierarchy under:

```text
/home/mahad
```

---

# `tree` Installation

`tree` may not be installed by default.

If Ubuntu reports:

```text
Command 'tree' not found
```

it can be installed with:

```bash
sudo apt install tree
```

Here:

- `sudo` runs the command with administrative privileges.
- `apt` is Ubuntu's package-management command.
- `install` tells `apt` to install a package.
- `tree` is the package being installed.

---

# Practical Example

Create a small directory structure:

```bash
mkdir sandbox
mkdir -p sandbox/projects/backend/spring

touch sandbox/notes.txt
```

Inspect it:

```bash
tree sandbox
```

Example:

```text
sandbox
├── notes.txt
└── projects
    └── backend
        └── spring

4 directories, 1 file
```

Check the file type:

```bash
file sandbox/notes.txt
```

Output:

```text
sandbox/notes.txt: empty
```

Inspect its metadata:

```bash
stat sandbox/notes.txt
```

This workflow combines directory creation, file creation, structural inspection, file-type detection, and metadata inspection.

---

# Quick Reference

```bash
# Directories
mkdir sandbox
mkdir dir1 dir2 dir3
mkdir -p projects/backend/spring
mkdir -pv projects/backend/spring

# Files
touch notes.txt
touch file1.txt file2.txt
touch -a notes.txt
touch -m notes.txt
touch -c notes.txt

# File information
file notes.txt
stat notes.txt

# Directory structure
tree
tree sandbox
tree -d
tree ~
```

---

# Key Takeaways

- `mkdir` creates directories.
- `mkdir -p` creates missing parent directories automatically.
- `mkdir -v` reports directories as they are created.
- `touch` can create empty files but is primarily used for managing timestamps.
- `touch -a` updates access time.
- `touch -m` updates modification time.
- `touch -c` prevents creation of a missing file.
- `file` identifies the type or contents of a filesystem object.
- `stat` provides detailed filesystem metadata.
- `tree` displays directory structures hierarchically.
- `tree -d` displays directories without ordinary files.
- Linux file types are not determined only by filename extensions.
