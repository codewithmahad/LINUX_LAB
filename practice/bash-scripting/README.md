# Bash practice

Small exercises from the lab. Run a file with `bash` from the repository root. Use Bash rather than `sh`; the examples include Bash arrays and conditional syntax.

| Exercise | Behaviour to check |
| :--- | :--- |
| [System report](01-basics/01-system-report.sh) | Read a project name and print the user, machine, directory, and timestamp. Keep spaces and backslashes intact. |
| [Session audit](01-basics/02-session-audit.sh) | Read application and environment labels; print the operating system and actual `BASH_VERSION`. |
| [Arithmetic](01-basics/03-arithmetic.sh) | Read two integers with up to nine digits and an optional leading minus. Interpret `08` as decimal; reject other formats and report division by zero with a failure status. |
| [Percentage](01-basics/04-percentage.sh) | Accept three whole-number marks from 0 to 100. Print the integer percentage and pass at 50% or above. |
| [Validated marks](03-loops/01-validated-marks.sh) | Retry invalid marks; accept 0–100 and pass at 40 or above. This exercise uses its own threshold. |
| [Number analysis](03-loops/02-number-analysis.sh) | Accept 1–100; skip multiples of three and report the remaining numbers, sum, count, and even count. For `8`: sum `27`, count `6`, even count `3`. |
| [Menu calculator](03-loops/03-menu-calculator.sh) | Repeat until exit. Accept unsigned operands with one to three digits; recover from invalid input and division by zero. |
| [Array operations](04-arrays/01-array-operations.sh) | Update, append, and remove items. Print three remaining values with their original indices: 1, 2, and 3. |
| [Marks statistics](04-arrays/02-marks-statistics.sh) | The sample gives total `290`, average `58`, minimum `33`, maximum `90`, three passes, and two failures. |
| [Second-largest distinct value](04-arrays/03-second-largest.sh) | The default sample gives `-7`. Optional integer arguments replace the sample; duplicates do not count as a second distinct value. |
| [Product lookup](04-arrays/04-product-lookup.sh) | Look up an exact, case-sensitive product name: Pen, Book, or Bag. Report other names as not found. |
| [Name collection](04-arrays/05-name-collection.sh) | Collect three full lines in an array and print them unchanged, including spaces, backslashes, or text such as `-n`. |

For example:

```bash
bash practice/bash-scripting/04-arrays/03-second-largest.sh 5 5 4
```

Expected output: `Second largest distinct number: 4`. With only one distinct value, the script reports the problem on stderr and returns a nonzero status.

Interactive scripts stop with a failure status if input ends before all required lines arrive. Empty text labels are allowed in the reporting examples; numeric exercises validate their input.

[Back to the lab](../../README.md#backend-practice)
