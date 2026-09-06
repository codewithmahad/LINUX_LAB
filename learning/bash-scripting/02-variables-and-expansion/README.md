# Variables and Expansion

Notes and examples from learning how Bash stores values and expands them before executing commands.

## Variables

Bash normally creates variables through assignment:

```bash
name="Mahad"
age=20
course="Operating Systems"
```

Unlike C++/Java, a separate declaration is usually unnecessary.

```bash
name="Mahad"
```

There must be no spaces around `=`:

```bash
name="Mahad"      # correct
name = "Mahad"    # incorrect
```

Whitespace separates command words in Bash, so the second form is interpreted as a command rather than an assignment.

## Using Variables

```bash
echo "$name"
echo "${name}"
```

Both expand the variable.

Braces are useful when text follows the variable name:

```bash
language="linux"

echo "${language}_lab"
```

Output:

```text
linux_lab
```

Without braces:

```bash
echo "$language_lab"
```

Bash would look for a variable named `language_lab`.

## Declaration with `declare`

Bash also provides `declare`:

```bash
declare message
message="Assigned later"
```

For ordinary variables this is usually unnecessary, but `declare` becomes useful for variable attributes.

Examples:

```bash
declare -i number=10
declare -a names
declare -A users
```

These represent an integer-attributed variable, indexed array, and associative array respectively.

## Unset vs Empty

An empty variable:

```bash
name=""
```

has been assigned an empty string.

An unset variable:

```bash
unset name
```

has no assigned value.

These are different states and become important when checking configuration and environment variables.

## Bash Values and Types

Bash is primarily string-oriented.

```bash
name="Mahad"
age=20
path="/home/mahad"
message="Linux and Bash"
```

Even numeric-looking scalar values are normally handled as shell data until used in an arithmetic context.

Bash does not use the normal C++/Java type system:

```text
int
float
double
char
bool
String
```

It also supports:

```text
scalar variables
indexed arrays
associative arrays
integer attributes
```

## Quoting

Double quotes allow expansion:

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

Variables should generally be quoted when used as strings:

```bash
echo "$name"
```

## Parameter Expansion

```bash
$name
${name}
```

Both retrieve the value of a parameter.

Example:

```bash
name="Mahad"

echo "${name}"
```

Output:

```text
Mahad
```

## Command Substitution

Command substitution runs a command and substitutes its output:

```bash
current_directory="$(pwd)"

echo "$current_directory"
```

Example output:

```text
/home/mahad/Github-Repo-Clones/LINUX_LAB
```

Preferred syntax:

```bash
$(command)
```

## Arithmetic Expansion

Bash needs an explicit arithmetic context:

```bash
number=10
result=$((number + 5))

echo "$result"
```

Output:

```text
15
```

`$(( ... ))` evaluates an arithmetic expression and substitutes its resulting value.

Coming from C++:

```cpp
int result = number + 5;
```

Bash instead uses:

```bash
result=$((number + 5))
```

because normal shell syntax is centered around commands and words rather than typed arithmetic expressions.

## Arithmetic Evaluation

Bash also supports:

```bash
(( ... ))
```

Example:

```bash
count=5
((count++))

echo "$count"
```

Output:

```text
6
```

Useful distinction:

```text
$((expression))    produce/substitute an arithmetic value
((expression))     evaluate an arithmetic expression
```

This becomes especially useful in loops and conditions.

## Integer Arithmetic

Bash's built-in arithmetic is integer-based.

```bash
result=$((10 / 3))

echo "$result"
```

Output:

```text
3
```

Normal Bash arithmetic does not provide C++/Java-style floating-point types such as `float` or `double`.

## Tilde Expansion

```bash
echo ~
```

Example output:

```text
/home/mahad
```

`~` expands to the current user's home directory.

## Expansion Summary

```text
$name             parameter expansion
${name}           explicit parameter expansion
$(command)        command substitution
$((expression))   arithmetic expansion
((expression))    arithmetic evaluation
~                 tilde expansion
```

A useful Bash mental model is:

```text
shell syntax
    ↓
expansion
    ↓
resulting command
    ↓
execution
```

## Examples

See:

```text
variables.sh
quoting.sh
expansions.sh
```