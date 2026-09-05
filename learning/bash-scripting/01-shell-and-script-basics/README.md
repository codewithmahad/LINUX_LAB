# Shell and Script Basics

Bash scripting allows shell commands to be stored in files and executed as repeatable programs.

This section covers the basic relationship between the terminal, shell, Bash, shell scripts, shebangs, execution methods, permissions, comments, and basic script validation.

---

## Terminal, Shell, and Bash

These terms are related but are not the same thing.

```text
User
  ↓
Terminal
  ↓
Shell
  ↓
Operating System
```

### Terminal

The terminal provides the interface where commands are entered and output is displayed.

Examples include the VS Code integrated terminal and standalone terminal applications.

### Shell

A shell is a command interpreter.

It reads commands, interprets shell syntax, and starts commands or programs.

Common shells include:

```text
Bash
sh
Zsh
Fish
Ksh
```

### Bash

Bash stands for:

```text
Bourne Again Shell
```

It is one specific shell and is widely used on Linux systems.

Check the configured login shell:

```bash
echo $SHELL
```

Example:

```text
/bin/bash
```

Check the installed Bash version:

```bash
bash --version
```

---

## What Is a Shell Script?

A shell script is a text file containing commands intended to be interpreted by a shell.

Instead of repeatedly entering:

```bash
echo "Starting"
pwd
date
echo "Finished"
```

the commands can be stored in a script and executed together.

Example:

```bash
#!/usr/bin/env bash

echo "Starting"
pwd
date
echo "Finished"
```

---

## The Shebang

A Bash script commonly begins with:

```bash
#!/usr/bin/env bash
```

The first two characters:

```text
#!
```

are called the **shebang**.

When the script is executed directly, the shebang tells the operating system which interpreter should handle the file.

Another common form is:

```bash
#!/bin/bash
```

`#!/bin/bash` uses Bash from a fixed location.

`#!/usr/bin/env bash` asks `env` to locate Bash through the current environment.

Both are commonly seen in Bash scripts.

---

## `echo`

`echo` prints text to standard output.

```bash
echo "Hello from Bash"
```

Output:

```text
Hello from Bash
```

Example script:

```bash
#!/usr/bin/env bash

echo "Hello from Bash"
```

---

## Sequential Execution

Normal Bash commands execute from top to bottom.

Example:

```bash
#!/usr/bin/env bash

echo "Script started"

pwd
date

echo "Script finished"
```

Possible output:

```text
Script started
/home/mahad/Github-Repo-Clones/LINUX_LAB/learning/bash-scripting/01-shell-and-script-basics
Sat Sep  5 16:30:00 PKT 2026
Script finished
```

The exact output of commands such as `date` depends on the system and current time.

---

## Comments

A normal Bash comment begins with `#`.

```bash
# Display the current directory
pwd
```

Bash ignores the comment.

Comments should normally explain something useful rather than restating obvious commands.

---

## Running a Script with Bash

A script can be passed explicitly to the Bash interpreter:

```bash
bash hello.sh
```

Here:

```text
bash       → interpreter
hello.sh   → script Bash should read
```

The file does not need executable permission for this execution method.

---

## Direct Script Execution

A script can also be executed directly:

```bash
./hello.sh
```

Here:

```text
.          current directory
/          path separator
hello.sh   script
```

The script must have executable permission.

Add it with:

```bash
chmod +x hello.sh
```

Then:

```bash
./hello.sh
```

can execute the script directly.

---

## Why `./` Is Needed

Typing:

```bash
hello.sh
```

does not normally make Bash search the current directory automatically.

Commands are searched for using directories listed in the `PATH` environment variable.

Therefore:

```bash
./hello.sh
```

explicitly identifies the script located in the current directory.

`PATH` is covered in more detail later.

---

## Two Execution Methods

| Command | Meaning |
| --- | --- |
| `bash script.sh` | Explicitly run the script using Bash |
| `./script.sh` | Execute the file directly |

For:

```bash
bash script.sh
```

executable permission is not required and Bash has already been explicitly chosen.

For:

```bash
./script.sh
```

the file needs executable permission and the shebang is used to select the interpreter.

---

## Script File Extension

Bash scripts do not technically require a `.sh` extension.

Both of these can be executable scripts:

```text
backup.sh
backup
```

The `.sh` extension is mainly a useful naming convention.

It is used throughout this repository for learning examples.

---

## Check Script Syntax

Bash can inspect a script for syntax errors without executing it:

```bash
bash -n script.sh
```

Example:

```bash
bash -n hello.sh
```

If the syntax is valid, Bash normally produces no output.

This is useful for validating a script before execution.

---

## Basic Script Workflow

```bash
touch script.sh
```

Add:

```bash
#!/usr/bin/env bash

echo "Hello"
```

Make it executable:

```bash
chmod +x script.sh
```

Check syntax:

```bash
bash -n script.sh
```

Execute through Bash:

```bash
bash script.sh
```

Or execute directly:

```bash
./script.sh
```

---

## Quick Reference

```bash
# Bash information
echo $SHELL
bash --version

# Run through Bash
bash script.sh

# Add executable permission
chmod +x script.sh

# Direct execution
./script.sh

# Check syntax without executing
bash -n script.sh
```

---

## Key Takeaways

Bash is a shell and command interpreter.

A shell script stores commands in a text file so they can be executed repeatedly.

The shebang specifies the interpreter for direct execution.

`bash script.sh` explicitly invokes Bash.

`./script.sh` directly executes the file and therefore requires executable permission.

`#` begins a normal Bash comment.

Scripts normally execute sequentially from top to bottom.

`.sh` is a naming convention rather than a technical requirement.

`bash -n` checks Bash syntax without executing the script.