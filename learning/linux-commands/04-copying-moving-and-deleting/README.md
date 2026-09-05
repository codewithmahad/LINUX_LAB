# Copying, Moving, and Deleting

Linux provides a small set of powerful commands for managing files and directories.

The main commands are:

```text
cp       copy
mv       move or rename
rm       remove
rmdir    remove empty directories
```

These commands modify filesystem data, so it is important to understand exactly what the source and destination arguments mean before running them.

---

# `cp` — Copy Files

Basic syntax:

```text
cp SOURCE DESTINATION
```

Example:

```bash
cp notes.txt notes-backup.txt
```

Suppose the directory initially contains:

```text
notes.txt
```

After the command:

```bash
ls
```

output may be:

```text
notes-backup.txt  notes.txt
```

The original file remains and a copy is created.

---

## Copy a File into Another Directory

```bash
cp notes.txt backups/
```

If `backups/` already exists:

```text
.
├── backups
│   └── notes.txt
└── notes.txt
```

The source remains unchanged.

---

## Copy and Rename at the Same Time

```bash
cp notes.txt backups/linux-notes.txt
```

This copies the file and gives the copy a different name.

Result:

```text
.
├── backups
│   └── linux-notes.txt
└── notes.txt
```

---

# `cp -r` — Copy Directories Recursively

A directory may contain other files and directories.

To copy the complete hierarchy, use:

```bash
cp -r project project-backup
```

`-r` means **recursive**.

Example source:

```text
project/
├── README.md
└── src/
    └── main.txt
```

After:

```bash
cp -r project project-backup
```

the structure becomes:

```text
.
├── project
│   ├── README.md
│   └── src
│       └── main.txt
└── project-backup
    ├── README.md
    └── src
        └── main.txt
```

Recursion means the command processes the directory and everything contained below it.

---

## `cp -i` — Ask Before Overwriting

```bash
cp -i notes.txt backup.txt
```

If `backup.txt` already exists, `cp` may ask:

```text
cp: overwrite 'backup.txt'?
```

`-i` means **interactive**.

This is useful when you want protection against accidentally replacing an existing file.

---

## `cp -v` — Verbose Output

```bash
cp -v notes.txt backup.txt
```

Example output:

```text
'notes.txt' -> 'backup.txt'
```

`-v` means **verbose**.

It shows what the command is doing.

Options can be combined:

```bash
cp -iv notes.txt backup.txt
```

---

## `cp -a` — Archive Copy

For copying complete directory trees while preserving important metadata, GNU `cp` provides:

```bash
cp -a project project-backup
```

`-a` means **archive**.

It is commonly useful when creating faithful filesystem copies because it recursively copies directories while preserving attributes such as permissions and timestamps where possible.

For ordinary directory copying:

```bash
cp -r
```

is usually sufficient.

For preservation-oriented copies:

```bash
cp -a
```

is often preferable.

---

# `mv` — Move Files and Directories

`mv` stands for **move**.

Basic syntax:

```text
mv SOURCE DESTINATION
```

Example:

```bash
mv notes.txt documents/
```

Before:

```text
.
├── documents
└── notes.txt
```

After:

```text
.
└── documents
    └── notes.txt
```

Unlike `cp`, the original does not remain in its old location.

---

# `mv` Also Renames Files

Linux does not require a separate basic `rename` command for simple renaming.

```bash
mv old-name.txt new-name.txt
```

Before:

```text
old-name.txt
```

After:

```text
new-name.txt
```

The same `mv` command therefore handles both:

- moving,
- renaming.

---

## Rename a Directory

```bash
mv old-project new-project
```

This renames the directory.

---

## Move and Rename Together

```bash
mv notes.txt documents/linux-notes.txt
```

This:

1. moves `notes.txt` into `documents/`,
2. renames it to `linux-notes.txt`.

---

## `mv -i` — Ask Before Overwriting

```bash
mv -i notes.txt destination.txt
```

If the destination already exists, `mv` may ask:

```text
mv: overwrite 'destination.txt'?
```

---

## `mv -v` — Verbose Output

```bash
mv -v notes.txt documents/
```

Example output:

```text
renamed 'notes.txt' -> 'documents/notes.txt'
```

Options can also be combined:

```bash
mv -iv notes.txt documents/
```

---

# `rm` — Remove Files

`rm` stands for **remove**.

```bash
rm notes.txt
```

If successful, it normally produces no output.

Before:

```text
notes.txt
```

After:

```text
```

The file is gone from that location.

---

## Important: `rm` Does Not Behave Like a Desktop Recycle Bin

A normal command such as:

```bash
rm notes.txt
```

does not normally move the file into the Windows Recycle Bin or a graphical Linux Trash folder.

For command-line work, treat `rm` as destructive.

Always verify paths before deleting important data.

---

# `rm -i` — Confirm Before Removing

```bash
rm -i notes.txt
```

Example prompt:

```text
rm: remove regular file 'notes.txt'?
```

Enter:

```text
y
```

to confirm.

`-i` means **interactive**.

---

# `rm -v` — Show What Was Removed

```bash
rm -v notes.txt
```

Example output:

```text
removed 'notes.txt'
```

---

# `rm -r` — Remove Directories Recursively

Plain `rm` cannot normally remove a directory:

```bash
rm project
```

Possible output:

```text
rm: cannot remove 'project': Is a directory
```

To delete a directory and everything inside it:

```bash
rm -r project
```

`-r` means **recursive**.

If:

```text
project/
├── README.md
└── src/
    └── main.txt
```

then:

```bash
rm -r project
```

removes:

```text
project/
README.md
src/
main.txt
```

as part of the recursive operation.

---

# `rm -f` — Force Removal

```bash
rm -f notes.txt
```

`-f` means **force**.

It suppresses certain prompts and errors, including complaints about nonexistent files.

For example:

```bash
rm -f missing.txt
```

normally produces no error even if `missing.txt` does not exist.

---

# `rm -rf` — Recursive Forced Removal

```bash
rm -rf directory
```

combines:

```text
-r    recursively remove directory contents
-f    force removal without normal confirmation
```

This command is powerful and potentially destructive.

For example:

```bash
rm -rf old-project
```

can remove the entire `old-project` hierarchy without asking for confirmation.

Before using `rm -rf`, verify the path carefully.

A mistake involving:

```bash
rm -rf
```

can destroy large amounts of data very quickly.

Avoid using it automatically when a safer command is sufficient.

---

# `rmdir` — Remove Empty Directories

`rmdir` removes directories only when they are empty.

```bash
rmdir empty-directory
```

If the directory is empty, it is removed.

If it contains something:

```bash
rmdir project
```

may produce:

```text
rmdir: failed to remove 'project': Directory not empty
```

This makes `rmdir` safer than recursive deletion when you specifically expect a directory to be empty.

---

## Remove Multiple Empty Directories

```bash
rmdir dir1 dir2 dir3
```

Each directory must be empty.

---

# Copy vs Move

Consider:

```bash
cp notes.txt backup.txt
```

Result:

```text
notes.txt
backup.txt
```

There are now two files.

Compare:

```bash
mv notes.txt backup.txt
```

Result:

```text
backup.txt
```

The original pathname `notes.txt` no longer exists.

Therefore:

```text
cp → preserves the source and creates another copy
mv → changes the source's location or name
```

---

# Source and Destination Matter

Many mistakes happen because the user misunderstands which argument is the source and which is the destination.

Remember:

```text
cp SOURCE DESTINATION
mv SOURCE DESTINATION
```

Example:

```bash
cp report.txt backups/
```

means:

```text
copy report.txt
       ↓
into backups/
```

Before running destructive filesystem commands, read them from left to right.

---

# Useful Safety Habit

Before running something destructive such as:

```bash
rm -r some-directory
```

inspect the target first:

```bash
ls some-directory
```

or:

```bash
tree some-directory
```

Then remove it only after confirming that the path is correct.

This simple habit prevents many mistakes.

---

# Practical Workflow Example

Create a file:

```bash
touch notes.txt
```

Copy it:

```bash
cp notes.txt notes-backup.txt
```

Output from:

```bash
ls
```

may be:

```text
notes-backup.txt  notes.txt
```

Create a directory:

```bash
mkdir documents
```

Move the original:

```bash
mv notes.txt documents/
```

Structure:

```text
.
├── documents
│   └── notes.txt
└── notes-backup.txt
```

Rename the backup:

```bash
mv notes-backup.txt old-notes.txt
```

Then remove it:

```bash
rm old-notes.txt
```

---

# Quick Reference

```bash
# Copy
cp source.txt copy.txt
cp source.txt directory/
cp -r source-directory backup-directory
cp -i source.txt destination.txt
cp -v source.txt destination.txt
cp -a source-directory backup-directory

# Move / rename
mv file.txt directory/
mv old-name.txt new-name.txt
mv old-directory new-directory
mv -i file.txt destination/
mv -v file.txt destination/

# Delete files
rm file.txt
rm -i file.txt
rm -v file.txt

# Delete directories
rmdir empty-directory
rm -r directory
rm -rf directory
```

---

# Key Takeaways

- `cp` copies files while leaving the source intact.
- `cp -r` recursively copies directories.
- `cp -a` performs a preservation-oriented archive copy.
- `cp -i` asks before overwriting.
- `mv` moves files and directories.
- `mv` is also used for ordinary renaming.
- `rm` removes files.
- `rm -r` recursively removes directory trees.
- `rm -f` forces removal and suppresses normal confirmation.
- `rm -rf` is powerful and should be used carefully.
- `rmdir` removes only empty directories.
- Always verify source and destination paths before filesystem operations.