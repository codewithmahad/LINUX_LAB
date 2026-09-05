# Viewing File Content

Linux provides several commands for reading files directly from the terminal.

The right command depends on whether you want to:

- display an entire file,
- inspect only the beginning or end,
- browse a large file interactively,
- or continuously watch new content being added.

---

## `cat` — Display File Content

`cat` stands for **concatenate**.

Its simplest use is displaying the complete contents of a file.

```bash
cat notes.txt
```

Example file:

```text
Linux
Bash
Git
Operating Systems
```

Command:

```bash
cat notes.txt
```

Output:

```text
Linux
Bash
Git
Operating Systems
```

`cat` works best for relatively small files that can be displayed comfortably in the terminal.

---

## Display Multiple Files

`cat` can accept multiple files.

```bash
cat file1.txt file2.txt
```

Suppose:

```text
file1.txt:
Linux Commands
```

and:

```text
file2.txt:
Bash Scripting
```

Running:

```bash
cat file1.txt file2.txt
```

produces:

```text
Linux Commands
Bash Scripting
```

This is where the name **concatenate** comes from: `cat` can combine file contents into one output stream.

---

## `cat -n` — Show Line Numbers

```bash
cat -n notes.txt
```

Example output:

```text
     1  Linux
     2  Bash
     3  Git
     4  Operating Systems
```

The `-n` option numbers all output lines.

This is useful when discussing or debugging a particular line in a text file.

---

# `head` — View the Beginning of a File

`head` displays the beginning of a file.

```bash
head notes.txt
```

By default, it displays the first **10 lines**.

Example:

```text
line 1
line 2
line 3
line 4
line 5
line 6
line 7
line 8
line 9
line 10
```

---

## Display a Specific Number of Lines

Use `-n`:

```bash
head -n 5 notes.txt
```

Output:

```text
line 1
line 2
line 3
line 4
line 5
```

Here:

```text
-n 5
```

means:

> Display the first 5 lines.

---

## Read Multiple Files

```bash
head file1.txt file2.txt
```

When multiple files are supplied, `head` identifies each file before displaying its content.

Example:

```text
==> file1.txt <==
Linux
Bash

==> file2.txt <==
Git
Docker
```

---

# `tail` — View the End of a File

`tail` displays the end of a file.

```bash
tail notes.txt
```

By default, it displays the last **10 lines**.

---

## Display a Specific Number of Lines

```bash
tail -n 5 notes.txt
```

Displays the last five lines.

Example:

```text
line 16
line 17
line 18
line 19
line 20
```

---

# `tail -f` — Follow a Growing File

One of the most useful forms of `tail` is:

```bash
tail -f application.log
```

The `-f` option means **follow**.

Instead of exiting after displaying the current end of the file, `tail` keeps running and displays new lines as they are added.

This is commonly used for:

- application logs,
- server logs,
- system logs,
- debugging running services.

Example:

```text
2026-09-05 16:10:01 Server started
2026-09-05 16:10:05 Client connected
2026-09-05 16:10:12 Request received
```

If another process adds:

```text
2026-09-05 16:10:20 Request completed
```

it appears automatically in the terminal.

Stop `tail -f` using:

```text
Ctrl + C
```

This is especially useful in backend development where logs change continuously.

---

# `less` — Browse Large Files

`less` opens a file in an interactive terminal viewer.

```bash
less large-file.txt
```

Unlike `cat`, it does not dump the entire file onto the terminal at once.

Instead, it lets you move through the file interactively.

This makes it better for:

- long text files,
- large logs,
- configuration files,
- command output.

---

## Useful `less` Controls

| Key | Action |
| --- | --- |
| `↑` / `↓` | Move one line |
| `Space` | Move one page forward |
| `b` | Move one page backward |
| `g` | Go to beginning |
| `G` | Go to end |
| `/text` | Search forward for text |
| `n` | Go to next search match |
| `N` | Go to previous search match |
| `q` | Quit |

Example:

```bash
less application.log
```

Inside `less`, type:

```text
/error
```

to search for the word `error`.

Press:

```text
n
```

to move to the next matching occurrence.

Press:

```text
q
```

to leave the viewer.

---

## Why `git log` Sometimes Opens a Similar Screen

Commands such as:

```bash
git log
```

often send their output through a **pager**, commonly `less`.

That is why Git output may appear in a screen where normal terminal typing seems unavailable.

Press:

```text
q
```

to exit.

The terminal itself is not frozen.

---

# `more` — Basic File Pager

`more` is another command for viewing long files page by page.

```bash
more notes.txt
```

Typical controls include:

```text
Space    next page
Enter    next line
q        quit
```

`more` is older and less flexible than `less`.

In most modern Linux work:

```bash
less
```

is generally preferred.

A common Linux joke is:

> `less` is more.

---

# Choosing the Right Command

| Goal | Command |
| --- | --- |
| Display a small file completely | `cat` |
| Display line numbers | `cat -n` |
| View first lines | `head` |
| View last lines | `tail` |
| Watch new log entries | `tail -f` |
| Browse a large file interactively | `less` |
| Basic page-by-page viewing | `more` |

---

# Practical Examples

Display an entire configuration file:

```bash
cat config.txt
```

Display it with line numbers:

```bash
cat -n config.txt
```

Inspect only the first five lines:

```bash
head -n 5 config.txt
```

Inspect the last twenty lines of a log:

```bash
tail -n 20 application.log
```

Monitor the log continuously:

```bash
tail -f application.log
```

Browse a large log interactively:

```bash
less application.log
```

---

# Quick Reference

```bash
# Display files
cat file.txt
cat -n file.txt
cat file1.txt file2.txt

# Beginning of files
head file.txt
head -n 5 file.txt

# End of files
tail file.txt
tail -n 5 file.txt
tail -f application.log

# Interactive viewing
less large-file.txt
more large-file.txt
```

---

# Key Takeaways

- `cat` displays or concatenates file contents.
- `cat -n` displays line numbers.
- `head` shows the beginning of a file.
- `tail` shows the end of a file.
- Both `head` and `tail` display 10 lines by default.
- `-n` controls how many lines are displayed.
- `tail -f` continuously follows files that are being updated.
- `less` is the preferred tool for interactively browsing large files.
- `/text` searches inside `less`.
- `q` exits `less` and many other terminal pagers.