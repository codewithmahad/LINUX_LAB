# Input and Output

Notes and examples covering basic terminal input and output in Bash using `echo`, `printf`, and `read`.

## `echo`

`echo` is useful for simple output.

```bash
name="Mahad"

echo "Hello, $name"
echo "Learning Bash"
```

Output:

```text
Hello, Mahad
Learning Bash
```

A blank `echo` prints an empty line:

```bash
echo
```

---

## `printf`

`printf` gives more control over formatting.

```bash
name="Mahad"
age=20
score=95

printf "Name: %s\n" "$name"
printf "Age: %d\n" "$age"
printf "Score: %d%%\n" "$score"
```

Output:

```text
Name: Mahad
Age: 20
Score: 95%
```

Common format sequences:

```text
%s    string
%d    integer
%%    literal %
\n    newline
```

Unlike `echo`, `printf` does not automatically append a newline.

```bash
printf "Hello"
printf "World"
```

Output:

```text
HelloWorld
```

Use:

```bash
printf "Hello\n"
```

when a newline is required.

---

## `read`

`read` accepts input from standard input and stores it in a variable.

```bash
read name
```

Example:

```bash
echo "Enter your name:"
read name

echo "Hello, $name"
```

Terminal:

```text
Enter your name:
Mahad
Hello, Mahad
```

Coming from C++:

```cpp
cin >> name;
```

is conceptually similar to:

```bash
read name
```

---

## `read -p`

`-p` displays a prompt before accepting input.

```bash
read -p "Enter your name: " name
```

Terminal:

```text
Enter your name: Mahad
```

---

## `read -r`

`-r` tells `read` not to treat backslashes as escape characters.

```bash
read -r -p "Enter a path: " path
```

For general text and paths, this is a good default:

```bash
read -r variable
```

---

## Reading Multiple Values

```bash
read -r -p "Enter first and last name: " first_name last_name
```

Input:

```text
Mahad Shaikh
```

Then:

```bash
echo "$first_name"
echo "$last_name"
```

Output:

```text
Mahad
Shaikh
```

Bash splits the input into fields and assigns them to the supplied variables.

---

## `read -s`

`-s` hides typed characters.

```bash
read -s -p "Password: " password
echo
```

Useful for sensitive terminal input.

The entered value still exists in the variable even though it is not displayed while typing.

---

## `REPLY`

If no variable name is supplied:

```bash
read -r
```

Bash stores the value in the special variable:

```text
REPLY
```

Example:

```bash
read -r -p "Enter something: "

echo "$REPLY"
```

---

## `echo` vs `printf`

```text
echo      simple output
printf    controlled/formatted output
```

Example:

```bash
echo "Hello, $name"

printf "Name: %s | Age: %d\n" "$name" "$age"
```

---

## Standard Input and Output

At this stage:

```text
read            receives input
echo / printf   produce output
```

These normally interact with:

```text
stdin     standard input
stdout    standard output
```

Redirection, pipelines, and `stderr` are covered separately later.

---

## Examples

See:

```text
output.sh
input.sh
formatted-output.sh
```

## Quick Reference

```bash
echo "Hello"
echo

printf "Name: %s\n" "$name"
printf "Age: %d\n" "$age"

read name
read -r name
read -p "Name: " name
read -r -p "Name: " name
read -s -p "Password: " password

read -r
echo "$REPLY"
```