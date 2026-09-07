[LINUX_LAB](../../../README.md) / [Bash scripting](../../../README.md#what-im-learning) / **02**

# Variables and Expansion

<picture>
  <source media="(max-width: 620px)" srcset="../../../assets/lessons/bash-variables-and-expansion-mobile.svg">
  <img src="../../../assets/lessons/bash-variables-and-expansion.svg" alt="Same variable, different quotes. Double quotes print Hello, Shaikh Mahad; single quotes print the literal Hello, $name." width="100%">
</picture>

My first scripts had every value written into the commands. Now I can name those values and reuse them. Coming from C++ and Java, variables are familiar; the bit I need to pay attention to is what Bash does with them **before a command runs**.

[Assignment](#give-a-value-a-name) · [Quotes](#the-quotes-change-the-command) · [Expansion](#what-bash-replaces) · [Try it](#your-turn-a-note-for-the-next-session) · [Revision](#quick-revision)

## Open the chapter

From the repo root, in a Bash terminal:

```bash
cd learning/bash-scripting/02-variables-and-expansion
```

Read the file, run it, then change a value. These three scripts only print output.

| In order | Run it | What to watch |
| :--- | :--- | :--- |
| [variables.sh](variables.sh) | `bash variables.sh` | Assign, reuse, and replace a value. |
| [quoting.sh](quoting.sh) | `bash quoting.sh` | Quotes change expansion and the arguments a command receives. |
| [expansions.sh](expansions.sh) | `bash expansions.sh` | Get a variable, command output, a calculation, or the home directory. |

Need a reminder on running `.sh` files? [Chapter 01](../01-shell-and-script-basics/README.md) has that setup.

## Give a value a name

```bash
name="Shaikh Mahad"
topic="Bash"
notebook="${topic}_notes"

echo "Student: $name"
echo "Notebook: $notebook"
```

This prints `Student: Shaikh Mahad` and `Notebook: Bash_notes`.

Three differences I keep in mind:

- **No type declaration needed.** `topic="Bash"` creates or updates the variable.
- **No spaces around `=`.** `topic = "Bash"` tries to run a command named `topic`.
- **Use `$` to read, not assign.** `$topic` and `${topic}` read the same value. Braces separate the name from a suffix: `$topic_notes` would look for a different variable.

An assignment stores the value at that moment. Changing `topic` later doesn't change the existing `notebook` value.

## The quotes change the command

```bash
name="Shaikh Mahad"
echo "Hello, $name"    # Hello, Shaikh Mahad
echo 'Hello, $name'    # Hello, $name
```

Double quotes allow variable expansion. Single quotes keep the text literal. Leaving quotes out introduces another problem: one value can become several arguments.

`echo` hides that difference by joining its arguments with spaces. Here, `printf '<%s>\n'` makes it visible: `%s` prints a string, `\n` ends the line, and `< >` are just markers. The format repeats for each argument:

```bash
message="Linux and Bash"
printf '<%s>\n' $message      # Deliberately unquoted for this comparison.
printf '<%s>\n' "$message"
```

```text
<Linux>
<and>
<Bash>
<Linux and Bash>
```

The first command receives three words; the second receives one string. Quoting the original assignment doesn't protect later uses of `$message`.

| Form | What happens |
| :--- | :--- |
| `"$message"` | Expands the value and keeps it as one argument, even if it's empty. |
| `'$message'` | Passes the literal text `$message`. |
| `$message` | Expands, then may split into words and expand wildcard patterns into filenames. An empty value can disappear. |

My default when passing a string to a command is **`"$variable"`**. [Chapter 03](../03-input-and-output/README.md#printf-when-the-output-needs-a-shape) builds on this with more `printf` formats.

## What Bash replaces

Expansion means Bash replaces a piece of shell syntax with its result. These are the forms I'm using so far:

| Form | Where the value comes from | Example |
| :--- | :--- | :--- |
| `$name` or `${name}` | A parameter, such as a variable | `echo "${topic}_notes"` |
| `$(command)` | The command's standard output | `current_directory="$(pwd)"` |
| `$((expression))` | An integer calculation | `next_session=$((sessions + 1))` |
| `~` | My home directory | `echo ~` |

```bash
sessions=3
current_directory="$(pwd)"
next_session=$((sessions + 1))

echo "Working in: $current_directory"
echo "Next session: $next_session"
```

The directory depends on where you run this. The next session is `4`. Writing `next_session="sessions + 1"` would just store that text, without calculating anything.

`$(pwd)` runs `pwd` and captures its output, removing trailing newlines. It doesn't save the command to run again later.

One exception to my quoting habit: `~` needs to be unquoted to expand. `echo "~"` prints a tilde. For a home path inside quotes, use `"$HOME"`, such as `"$HOME/linux-lab-practice"`.

<details>
<summary><strong>For revision: empty, unset, and declare</strong></summary>

`note=""` assigns an empty string. `unset note` removes the variable. With Bash's usual settings, `echo "$note"` looks blank in both cases, but they are different states. That matters later when a script needs to distinguish a missing setting from an intentionally empty one.

`declare message` is valid, but ordinary assignments don't need it. `declare` also supports attributes and arrays; I'll give those space when I reach those topics.

</details>

## Your turn: a note for the next session

Before running this, predict the last three lines:

```bash
topic="Bash"
session=3
note="${topic}_session_$((session + 1))"
topic="Linux"

echo "$note"
echo '$note'
echo "$topic"
```

<details>
<summary><strong>Check your prediction</strong></summary>

```text
Bash_session_4
$note
Linux
```

`note` was built when `topic` was `Bash`. Single quotes keep `$note` literal. The final line reads the updated topic. Move the `topic="Linux"` assignment above the `note` assignment and try again.

</details>

## Quick revision

| If I forget… | The reminder I need |
| :--- | :--- |
| Why an assignment fails | Check spaces around `=` before anything else. |
| Why a value became separate words | Quote the expansion where I use it. |
| Which parentheses to use | `$(...)` captures output; `$((...))` calculates. `((...))` and its status come in [chapter 04](../04-operators-and-expressions/README.md#exit-status). |

<details>
<summary><strong>References for the details</strong></summary>

GNU Bash manual: [quoting](https://www.gnu.org/software/bash/manual/html_node/Quoting.html), [shell expansions](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html), and [command substitution](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html). Offline, `man bash` has the same topics.

</details>

[← Bash 01: Shell and Script Basics](../01-shell-and-script-basics/README.md) · [Back to the learning map](../../../README.md#what-im-learning)

**[Next: Bash 03, Input and Output →](../03-input-and-output/README.md)** Now the person running the script can supply the values.
