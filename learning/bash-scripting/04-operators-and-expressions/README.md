# Operators and Expressions

Notes and examples covering Bash arithmetic, comparisons, logical expressions, and command chaining.

## Arithmetic Operators

Bash arithmetic is evaluated inside an arithmetic context.

```bash
first=17
second=5

sum=$((first + second))
difference=$((first - second))
product=$((first * second))
quotient=$((first / second))
remainder=$((first % second))
```

Common operators:

| Operator | Meaning |
| --- | --- |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Integer division |
| `%` | Remainder |
| `**` | Exponentiation |

Example:

```bash
result=$((2 ** 8))
echo "$result"
```

Output:

```text
256
```

Bash's built-in arithmetic is integer-based.

```bash
echo $((10 / 3))
```

Output:

```text
3
```

## Arithmetic Expansion vs Evaluation

Arithmetic expansion:

```bash
result=$((number + 5))
```

`$(( ... ))` evaluates an expression and substitutes its value.

Arithmetic evaluation:

```bash
((number += 5))
```

`(( ... ))` performs/evaluates arithmetic without requiring the value to be substituted into another command.

A useful distinction:

```text
$(( expression ))   produce a value
(( expression ))    evaluate arithmetic
```

## Assignment and Update Operators

Inside arithmetic context, Bash supports familiar C/C++-style operators:

```bash
((count++))
((count--))

((count += 5))
((count -= 5))
((count *= 2))
((count /= 2))
((count %= 3))
```

## Numeric Comparisons

Inside `(( ... ))`, numeric comparisons look similar to C++:

```bash
(( first == second ))
(( first != second ))
(( first < second ))
(( first <= second ))
(( first > second ))
(( first >= second ))
```

These expressions produce an exit status:

```text
0    true / success
1    false
```

Example:

```bash
first=20
second=15

(( first > second ))
echo "$?"
```

Output:

```text
0
```

Traditional shell test syntax also provides numeric comparison operators:

```text
-eq    equal
-ne    not equal
-lt    less than
-le    less than or equal
-gt    greater than
-ge    greater than or equal
```

Example:

```bash
[ "$first" -gt "$second" ]
echo "$?"
```

## String Expressions

`[[ ... ]]` is commonly used for Bash string expressions.

```bash
username="mahad"

[[ "$username" == "mahad" ]]
[[ "$username" != "admin" ]]
```

Useful string tests:

```text
==    strings match
!=    strings differ
-n    string is non-empty
-z    string is empty
```

Examples:

```bash
[[ -n "$username" ]]
[[ -z "$empty_value" ]]
```

## `(( ))`, `[[ ]]`, and `[ ]`

These constructs serve different purposes.

```text
(( ... ))    arithmetic expressions
[[ ... ]]    Bash conditional/test expressions
[ ... ]      traditional test syntax
```

Examples:

```bash
(( age >= 18 ))

[[ "$name" == "Mahad" ]]

[ "$age" -ge 18 ]
```

For Bash-specific scripts, `(( ... ))` is generally convenient for numbers and `[[ ... ]]` for string/file expressions.

Traditional `[ ... ]` syntax is still common and important to recognize.

## Logical Operators

Logical expressions can use:

```text
&&    AND
||    OR
!     NOT
```

Example:

```bash
[[ "$role" == "student" && "$active" == "yes" ]]
```

Another example:

```bash
[[ "$role" == "admin" || "$role" == "student" ]]
```

Negation:

```bash
[[ ! "$role" == "admin" ]]
```

## Exit Status

Shell expressions and commands communicate success or failure through an exit status.

```text
0          success / true
non-zero   failure / false
```

`$?` contains the exit status of the most recently executed command.

```bash
ls .
echo "$?"
```

Typical output:

```text
0
```

For something that fails:

```bash
ls missing-directory
echo "$?"
```

the status will be non-zero.

## Command Chaining

`&&` and `||` can also connect complete commands.

```bash
command1 && command2
```

`command2` runs only if `command1` succeeds.

```bash
mkdir -p project && echo "Directory ready"
```

With OR:

```bash
command1 || command2
```

`command2` runs only if `command1` fails.

```bash
ls missing-directory || echo "Directory not found"
```

This behavior is based on command exit statuses rather than Java/C++ Boolean variables.

## Operator Precedence

Arithmetic precedence works similarly to C++.

```bash
echo $((2 + 3 * 4))
```

Output:

```text
14
```

Grouping changes the result:

```bash
echo $(((2 + 3) * 4))
```

Output:

```text
20
```

## Examples

```text
arithmetic.sh
assignment-and-update.sh
numeric-comparisons.sh
string-comparisons.sh
logical-expressions.sh
command-chaining.sh
```

## Quick Reference

```bash
result=$((a + b))

((count++))
((count += 5))

((a >= b))

[[ "$name" == "Mahad" ]]
[[ -n "$name" ]]
[[ -z "$value" ]]

[ "$a" -gt "$b" ]

command1 && command2
command1 || command2

echo "$?"
```