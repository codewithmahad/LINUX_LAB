# Variables and Expansion

Notes and examples covering basic Bash variables, quoting, and common forms of shell expansion.

## Variables

Create a variable:

```bash
name="Mahad"
course="Operating Systems"
semester=4
```

There must be no spaces around `=`.

```bash
name="Mahad"      # correct
name = "Mahad"    # incorrect
```

Use a variable with:

```bash
echo "$name"
```

or:

```bash
echo "${name}"
```

Braces are useful when additional text follows the variable name:

```bash
name="linux"

echo "${name}_lab"
```

Output:

```text
linux_lab
```

## Quoting

Double quotes allow variable expansion:

```bash
name="Mahad"

echo "Hello, $name"
```

Output:

```text
Hello, Mahad
```

Single quotes preserve text literally:

```bash
echo 'Hello, $name'
```

Output:

```text
Hello, $name
```

In general, variables should be quoted when used as strings:

```bash
echo "$name"
```

This avoids problems with spaces and shell word splitting.

## Parameter Expansion

```bash
name="Mahad"

echo "${name}"
```

`${name}` expands to the value stored in `name`.

## Command Substitution

Command substitution captures the output of another command:

```bash
current_directory="$(pwd)"

echo "$current_directory"
```

Example output:

```text
/home/mahad/Github-Repo-Clones/LINUX_LAB/learning/bash-scripting/02-variables-and-expansion
```

Preferred syntax:

```bash
$(command)
```

## Arithmetic Expansion

Bash supports integer arithmetic using:

```bash
$((expression))
```

Example:

```bash
year=2026
next_year=$((year + 1))

echo "$next_year"
```

Output:

```text
2027
```

## Tilde Expansion

`~` expands to the current user's home directory.

```bash
echo ~
```

Example:

```text
/home/mahad
```

## Expansion Overview

Some common expansions used by Bash are:

```text
$name           variable/parameter expansion
${name}         explicit parameter expansion
$(command)      command substitution
$((expression)) arithmetic expansion
~               home-directory expansion
```

Bash performs expansions while interpreting a command before the resulting command is executed.

## Examples

See:

```text
variables.sh
quoting.sh
expansions.sh
```

## Quick Reference

```bash
name="Mahad"

echo "$name"
echo "${name}"

echo 'Literal $name'
echo "Expanded $name"

directory="$(pwd)"

number=10
result=$((number + 5))

echo ~
```