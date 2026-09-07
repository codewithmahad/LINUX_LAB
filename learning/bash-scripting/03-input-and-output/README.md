[LINUX_LAB](../../../README.md) / [Bash scripting](../../../README.md#what-im-learning) / **03**

# Input and Output

<picture>
  <source media="(max-width: 620px)" srcset="../../../assets/lessons/bash-input-and-output-mobile.svg">
  <img src="../../../assets/lessons/bash-input-and-output.svg" alt="A script asks Enter your name. Shaikh Mahad is entered, stored in name, and printed as Name: Shaikh Mahad." width="100%">
</picture>

In the last chapter, I put my name into a variable myself. Here, the script asks for it. This is enough to turn a fixed message into a small check-in I can actually use.

I already know what input and output do from C++ and Java. These notes focus on the Bash parts: keeping a full line intact, choosing a format, and remembering where the newline goes.

[Print](#echo-for-a-simple-message) · [Format](#printf-when-the-output-needs-a-shape) · [Read](#read-a-line-without-changing-it) · [Try it](#your-turn-a-session-check-in) · [Revision](#quick-revision)

## Open the chapter

From the repo root, in a Bash terminal:

```bash
cd learning/bash-scripting/03-input-and-output
```

| In order | Run it | What to watch |
| :--- | :--- | :--- |
| [output.sh](output.sh) | `bash output.sh` | A greeting and a blank line with `echo`. |
| [formatted-output.sh](formatted-output.sh) | `bash formatted-output.sh` | Strings, integers, and a literal percent sign with `printf`. |
| [input.sh](input.sh) | `bash input.sh` | Two prompts, then a summary of the values you entered. |

All three print to the terminal. They don't create or change files.

## echo for a simple message

```bash
name="Shaikh Mahad"
echo "Hello, $name"
echo
echo "Back to Bash."
```

`echo` adds a newline after its arguments. An `echo` on its own gives me a blank line. For a fixed message like this, that's all I need.

For arbitrary text or formatting, I use `printf`. `echo` can interpret values such as `-n` as options, and its backslash handling depends on the shell and settings.

## printf when the output needs a shape

```bash
name="Shaikh Mahad"
sessions=3
score=95

printf 'Name: %s\n' "$name"
printf 'Sessions: %d\n' "$sessions"
printf 'Score: %d%%\n' "$score"
```

```text
Name: Shaikh Mahad
Sessions: 3
Score: 95%
```

| In the format | Meaning |
| :--- | :--- |
| `%s` | Insert a string. |
| `%d` | Format an integer. It doesn't validate arbitrary user input. |
| `%%` | Print a literal `%`. |
| `\n` | Print a newline. `printf` doesn't add one automatically. |

The format stays fixed; values go in separate, quoted arguments:

```bash
message='100% ready for the next script.'
printf '%s\n' "$message"
```

This prints the message exactly, followed by a newline. `printf "$message"` would treat the message itself as a format, so `%` and backslashes could change the output.

## read a line without changing it

This is the input line from [input.sh](input.sh):

```bash
IFS= read -r -p "Enter your name: " name || exit 1
```

| Part | Why it's here |
| :--- | :--- |
| `IFS=` | Sets the input field separator to empty for this `read` only, so it doesn't split or trim whitespace. |
| `read` | Reads a line from standard input, without storing its ending newline. |
| `-r` | Keeps backslashes literal. A useful default for text. |
| `-p "..."` | Shows a prompt when reading from a terminal. |
| `name` | The variable to fill. No `$` when giving its name. |
| `\|\| exit 1` | `\|\|` runs the command on its right only if `read` fails. `exit 1` ends the script with a failure status. |

With one variable and `IFS=`, this behaves more like reading a whole line with C++ `getline` than reading a single word with `cin >>`.

If the input ends before a complete line is read, the script stops instead of printing an incomplete summary. In a terminal, Ctrl+D on an empty input line signals end-of-file. [Chapter 04](../04-operators-and-expressions/README.md#command-chaining) uses the same `||` rule with other commands.

Run `bash input.sh` and enter two lines:

```text
Enter your name: Shaikh Mahad
Enter your course: Operating Systems

Student information
Name: Shaikh Mahad
Course: Operating Systems
```

Try a name with spaces or a course containing `100%`. Both should come back unchanged. Pressing Enter on an empty line is valid input here; this example preserves text, but doesn't require a nonempty value.

<details>
<summary><strong>A few read options I'll want to find again</strong></summary>

**Split a line into fields** when that's intentional:

```bash
read -r -p "First and last name: " first_name last_name
printf 'First: %s\nLast: %s\n' "$first_name" "$last_name"
```

With the usual space/tab delimiters, `Shaikh Mahad` becomes `Shaikh` and `Mahad`. Extra words go into the last variable. Leaving off `IFS=` allows that splitting and trims surrounding delimiter whitespace.

**Hide typed characters** in a terminal:

```bash
IFS= read -r -s -p "Password: " password
printf '\n'
unset password
```

`-s` hides typing; it doesn't encrypt the value. Don't print it back. This snippet discards it after the demonstration.

**Omit the variable name** and Bash stores the line in `REPLY`:

```bash
read -r -p "One thing to revise: "
printf '%s\n' "$REPLY"
```

</details>

## Your turn: a session check-in

Make a copy of `input.sh` for practice. Replace its course prompt with a topic prompt, then add a line asking what to revise next. Print all three answers with `printf`.

Try `Bash quoting` as the topic and `paths with spaces` as the reminder. The words should stay together.

<details>
<summary><strong>The extra prompt and output</strong></summary>

Inside your script, after reading the name:

```bash
IFS= read -r -p "Today's topic: " topic || exit 1
IFS= read -r -p "Next time, revise: " reminder || exit 1

printf '\nStudent: %s\nTopic: %s\nNext: %s\n' "$name" "$topic" "$reminder"
```

You can keep several `%s` fields in one format. The arguments fill them in order.

</details>

## Quick revision

| If I forget… | The reminder I need |
| :--- | :--- |
| Why two outputs run together | `printf` needs an explicit `\n`. |
| Why spaces or backslashes changed | Check `IFS=` and `read -r`. Quoting the output alone can't recover lost input. |
| Why `%` behaves strangely | Keep the `printf` format separate from the value. |
| Where the data goes | `read` uses standard input; `echo` and `printf` use standard output. The terminal is just their usual destination here. |

Pipes and redirection can connect those streams to commands and files. I've already used some in [Text Processing](../../linux-commands/06-text-processing/README.md); I'll return to them as the scripts grow.

<details>
<summary><strong>References for the details</strong></summary>

GNU Bash manual: [Bash builtins](https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html), including `echo`, `printf`, and `read`. In a Bash terminal, `help read` and `help printf` are useful offline references.

</details>

[← Bash 02: Variables and Expansion](../02-variables-and-expansion/README.md) · [Back to the learning map](../../../README.md#what-im-learning)

**[Next: Bash 04, Operators and Expressions →](../04-operators-and-expressions/README.md)** Calculate with the values and check whether a command succeeded.
