[LINUX_LAB](../../../README.md) / [Linux commands](../../../README.md#what-im-learning) / **06**

# Text Processing

<picture>
  <source media="(max-width: 620px)" srcset="../../../assets/lessons/text-processing-mobile.svg">
  <img src="../../../assets/lessons/text-processing.svg" alt="A few lines. A useful answer. The six entries in labels.txt become three counts: bash 2, git 1, linux 3." width="100%">
</picture>

Last chapter was about finding things. This one is about making something useful out of what we found. A list of topics can become a count. A file of study sessions can tell me which topics need another look.

I don't want to memorise seven commands as seven separate definitions. I'd rather give each one a small job and check the result.

[Get the files](#three-files-to-work-with) · [Count](#wc-how-much-text-is-here) · [Pick columns](#cut-keep-the-fields-you-need) · [Sort](#sort-put-the-lines-in-order) · [Count repeats](#uniq-repeated-lines-have-to-be-neighbours) · [Change text](#tr-change-characters) · [Use awk](#awk-ask-a-question-about-each-row) · [Practise](#your-turn-make-a-small-study-report)

> **By the end:** count, select, sort, summarise, and transform plain text, with output you can explain.
>
> **Before starting:** use Bash on Linux or Ubuntu in WSL. [Viewing File Content](../03-viewing-file-content/README.md) and [Searching and Finding](../05-searching-and-finding/README.md) are useful foundations. The files below are included in this chapter.

## Three files to work with

From the root of your cloned `LINUX_LAB` repo:

```bash
cd learning/linux-commands/06-text-processing
ls examples
```

Open the sample session records:

```bash
cat examples/sessions.txt
```

```text
navigation:12:done
files:8:done
viewing:20:review
copying:5:review
searching:15:done
```

These are **made-up practice records**, not my actual study times. Each line has three fields separated by a colon: **topic : minutes : status**. There is no header row.

| File | What we'll use it for |
| :--- | :--- |
| [sessions.txt](examples/sessions.txt) | Count records, select fields, sort numbers, and filter rows. |
| [labels.txt](examples/labels.txt) | See why duplicate lines need special attention. |
| [message.txt](examples/message.txt) | Try character changes and word replacements. |

Stay in this chapter folder. The examples print their results to the terminal and leave these source files unchanged.

## Choose the job first

| If I want to… | Tool |
| :--- | :--- |
| Count lines, words, or bytes | `wc` |
| Keep particular fields from every line | `cut` |
| Put lines in order | `sort` |
| Collapse or count adjacent repeated lines | `uniq` |
| Translate or remove individual characters | `tr` |
| Replace matching text or select line ranges | `sed` |
| Select rows, use fields, or calculate a total | `awk` |

`sed` and `awk` have much more to them. Here I'm learning a few useful patterns I can read properly before making them longer.

## Wc: how much text is here?

```bash
wc -l examples/sessions.txt
```

```text
5 examples/sessions.txt
```

There are five records. `wc -l` counts **newline characters**; every record in our sample ends with one. If the final line of another file has no ending newline, `wc -l` won't count that unfinished line.

| Option | Counts |
| :--- | :--- |
| `-l` | Newlines. |
| `-w` | Words separated by whitespace. |
| `-c` | Bytes. |
| `-m` | Characters, using the active locale. |

With no options, `wc file` prints newline, word, and byte counts in that order, then the filename. Padding around the numbers can vary.

**A small catch:** a colon isn't whitespace. `wc -w examples/sessions.txt` also reports **5**, because each whole record is one whitespace-separated word. It doesn't know that our data has three fields. Bytes and characters can also differ when a file contains text such as Urdu letters or emoji.

## Cut: keep the fields you need

Let's take only the topic names:

```bash
cut -d ':' -f 1 examples/sessions.txt
```

```text
navigation
files
viewing
copying
searching
```

`-d ':'` chooses the delimiter, and `-f 1` selects the first field. Field numbering starts at **1**. Without `-d`, the field delimiter is a tab.

To keep the topic and status:

```bash
cut -d ':' -f 1,3 examples/sessions.txt
```

```text
navigation:done
files:done
viewing:review
copying:review
searching:done
```

Use `-f 1-2` for fields one through two. `cut` selects fields from every line; [grep](../05-searching-and-finding/README.md#grep-find-the-lines-that-matter) selects matching lines.

<details>
<summary><strong>What cut assumes about the file</strong></summary>

These examples have one colon between fields and no colons inside a value. That makes `cut` a good fit.

- Lines without the delimiter pass through unchanged by default. Add `-s` to suppress those lines.
- `cut -d ' '` treats each space as a separator. It doesn't group runs of spaces into a single separator; default `awk` field splitting is often more useful for that.
- `cut -d ','` does not understand quoted CSV. A comma inside a quoted value still gets treated as a delimiter. Use a CSV-aware tool when your data needs one.

</details>

## Sort: put the lines in order

```bash
sort examples/labels.txt
```

```text
bash
bash
git
linux
linux
linux
```

Sorting puts repeated lines together. It doesn't remove them. The original `labels.txt` still has its original order; check with `cat examples/labels.txt`.

### Numbers need a numeric sort

Now arrange the session records by minutes:

```bash
sort -t ':' -k2,2n examples/sessions.txt
```

```text
copying:5:review
files:8:done
navigation:12:done
searching:15:done
viewing:20:review
```

`-t ':'` sets the field separator for `sort`. `-k2,2n` uses **only field 2** as a numeric key. The second `2` matters: it ends the key at that field instead of letting it run through the rest of the line.

Try the same command with `-k2,2` instead. The minutes come out as **12, 15, 20, 5, 8**, because that comparison treats them as text. Add `r` to the numeric key, `-k2,2nr`, for largest first.

<details>
<summary><strong>Why sort order can vary between systems</strong></summary>

Text sorting follows your locale's collation rules. Case, accents, and punctuation can affect the order. To request byte-based ordering for a command, use:

```bash
LC_ALL=C sort examples/labels.txt
```

This environment assignment applies to that command. It doesn't permanently change your terminal's locale. Our simple lowercase labels give the displayed order in the usual Ubuntu locales and in `C`.

</details>

## Uniq: repeated lines have to be neighbours

Here is the original `labels.txt`, with repeats deliberately spread out:

```text
bash
linux
linux
git
bash
linux
```

Try:

```bash
uniq examples/labels.txt
```

```text
bash
linux
git
bash
linux
```

Only the two neighbouring `linux` lines collapsed. The later `bash` and `linux` entries are still there. **`uniq` compares adjacent lines**, so it doesn't need sorted input, but sorting first brings all identical lines together.

### A first look at a pipe

```bash
sort examples/labels.txt | uniq -c
```

```text
      2 bash
      1 git
      3 linux
```

The shell's `|` sends the output of `sort` into `uniq` as input. `-c` adds a count for each group. You don't need an intermediate file. We'll explore pipes properly in chapter 07; this one is enough to make the duplicate-counting example work.

For just the three distinct labels, use `sort -u examples/labels.txt`. Here, `-u` belongs to **sort**. `uniq -u` has a different meaning: it prints only groups that occur once. After sorting this sample, that would be just `git`.

## Tr: change characters

Our small message is:

```text
linux is fun. linux takes practice.
```

Make its letters uppercase:

```bash
tr '[:lower:]' '[:upper:]' < examples/message.txt
```

```text
LINUX IS FUN. LINUX TAKES PRACTICE.
```

`tr` reads **standard input**, so it doesn't accept an input filename the way `cat` does. The shell's `<` feeds it this file. The quoted character classes identify lowercase and uppercase letters; our example uses ASCII text.

To delete the full stops from the output:

```bash
tr -d '.' < examples/message.txt
```

```text
linux is fun linux takes practice
```

`tr` works with individual characters. `tr 'linux' 'ubuntu'` would map characters rather than replace the word `linux`. For a text replacement, I want `sed`.

## Sed: try a replacement

```bash
sed 's/linux/Linux/' examples/message.txt
```

```text
Linux is fun. linux takes practice.
```

Read `s/linux/Linux/` as “substitute `linux` with `Linux`”. By default, that replaces the first match **on each line**. Add `g` to replace every match on each line:

```bash
sed 's/linux/Linux/g' examples/message.txt
```

```text
Linux is fun. Linux takes practice.
```

Run `cat examples/message.txt` again. Both words are still lowercase in the source. These commands print a changed version; they don't save over the file. The search part is a regular expression, so the pattern rules from [Searching and Finding](../05-searching-and-finding/README.md#a-little-pattern-matching) matter here too.

<details>
<summary><strong>Select a line range with sed</strong></summary>

```bash
sed -n '2,4p' examples/sessions.txt
```

```text
files:8:done
viewing:20:review
copying:5:review
```

`-n` suppresses the usual automatic printing. `2,4p` prints lines two through four. Without `-n`, these selected lines would appear twice: once automatically and once because of `p`.

Different tools reuse short options. Here `-n` means quiet automatic output; in `head -n 3` it sets a line count.

</details>

## Awk: ask a question about each row

`awk` reads records and splits them into fields. With its default settings, a line is a record and runs of spaces or tabs separate fields. Our file uses colons, so we'll set `-F ':'`.

Which topics need a review, and how many minutes were spent on them?

```bash
awk -F ':' '$3 == "review" {print $1, $2}' examples/sessions.txt
```

```text
viewing 20
copying 5
```

| Piece | Meaning |
| :--- | :--- |
| `-F ':'` | Split each record at colons. |
| `$3 == "review"` | Select records whose third field is exactly `review`. |
| `{print $1, $2}` | Print their first two fields, separated by a space by default. |

In `awk`, `$1` is field one, `$2` is field two, and `$0` is the entire current record. The single quotes around the program keep **Bash** from expanding those `$` expressions before `awk` receives them.

### Add the minutes

```bash
awk -F ':' '{total += $2} END {print total}' examples/sessions.txt
```

```text
60
```

For each record, `total += $2` adds its minutes. The variable starts with a numeric value of zero when first used in this addition. `END` runs after all the input has been read, so we print one final total.

This works because every second field in our sample is numeric and there is no header. With a different file, check its format first. These introductory examples work with common Linux `awk` implementations, including the `mawk` often used on Ubuntu; they don't require GNU-only extensions.

## Your turn: make a small study report

Use the supplied files and try these before opening the answers:

1. Print only the names of topics marked `done`.
2. Put the session records in order from most minutes to fewest.
3. Print a version of `sessions.txt` where the status `review` becomes `next`.
4. Count each label. Check that the counts add up to the original number of lines.
5. **One extra step:** add up only the minutes from records marked `review`.

<details>
<summary><strong>Compare your report</strong></summary>

```bash
awk -F ':' '$3 == "done" {print $1}' examples/sessions.txt
sort -t ':' -k2,2nr examples/sessions.txt
sed 's/:review$/:next/' examples/sessions.txt
sort examples/labels.txt | uniq -c
wc -l examples/labels.txt
awk -F ':' '$3 == "review" {total += $2} END {print total + 0}' examples/sessions.txt
```

1. The names are **navigation**, **files**, and **searching**, in that order.
2. The minutes are **20, 15, 12, 8, 5**. Their complete records stay together.
3. The viewing and copying records now end in `:next` in the output. The `$` in the pattern anchors `review` to the end of the line. The file is unchanged.
4. **2 bash + 1 git + 3 linux = 6 lines**, matching `wc -l`.
5. The result is **25**, from `20 + 5`. `total + 0` also ensures that a numeric zero prints if a different input has no matching records.

</details>

## Things I'd check before blaming the command

| Surprise | Check |
| :--- | :--- |
| `sort` puts `12` before `5`. | Request a numeric key with `n`. |
| `uniq` leaves repeated labels. | Only adjacent repeats are compared. Sort first if order doesn't need to be preserved. |
| `cut` gives unexpected fields. | Check the actual delimiter and whether values contain it. |
| `tr` complains about extra operands. | Supply the file through `<`; it doesn't take a file operand. |
| `sed` changes only one occurrence per line. | Add the `g` flag when you want all occurrences on each line. |
| `awk` behaves strangely after changing the quotes. | Keep the program in single quotes so Bash leaves `$1`, `$2`, and `$3` alone. |
| A transformed file still looks the same when opened. | These commands print results. Saving output is a separate shell operation. |

## Quick revision

| Job | Command from this chapter |
| :--- | :--- |
| Count records | `wc -l examples/sessions.txt` |
| Extract minutes | `cut -d ':' -f 2 examples/sessions.txt` |
| Sort by minutes | `sort -t ':' -k2,2n examples/sessions.txt` |
| List distinct labels | `sort -u examples/labels.txt` |
| Count each label | `sort examples/labels.txt \| uniq -c` |
| Capitalise the message | `tr '[:lower:]' '[:upper:]' < examples/message.txt` |
| Replace every `linux` | `sed 's/linux/Linux/g' examples/message.txt` |
| Print review topics | `awk -F ':' '$3 == "review" {print $1}' examples/sessions.txt` |

**Before moving on:** explain the difference between selecting a line and selecting a field. Then explain why `sort` comes before `uniq -c`, and why neither command changes `labels.txt` here.

<details>
<summary><strong>References behind these notes</strong></summary>

- GNU Coreutils: [wc](https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html), [cut](https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html), [sort](https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html), [uniq](https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html), and [tr](https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html).
- GNU Sed: [the substitution command](https://www.gnu.org/software/sed/manual/html_node/The-_0022s_0022-Command.html) and [manual](https://www.gnu.org/software/sed/manual/sed.html).
- GNU Awk: [fields](https://www.gnu.org/software/gawk/manual/html_node/Fields.html) and [printing output](https://www.gnu.org/software/gawk/manual/html_node/Printing.html).
- Local manuals: `man wc`, `man cut`, `man sort`, `man uniq`, `man tr`, `man sed`, and `man awk`.
- [Chapter artwork and Tux credit](../../../assets/README.md#lesson-covers).

</details>

## Small commands start working together

We used one pipe to count labels and one input redirection to feed `tr`. Next in the sequence is **07: Redirection and Pipes**, where I want to cover connecting commands and saving their output properly.

That chapter isn't published yet. For now, [revisit Searching and Finding](../05-searching-and-finding/README.md), try changing a pattern in these examples, or [open the Bash notes on input and output](../../bash-scripting/03-input-and-output/README.md).

[Previous: Searching and Finding](../05-searching-and-finding/README.md) · [All learning topics](../../../README.md#what-im-learning) · [Back to the top](#text-processing)

Notes by **Shaikh Mahad**. Found a clearer way to explain a command? [Open an issue](https://github.com/codewithmahad/LINUX_LAB/issues). That's useful feedback for my next revision too.
