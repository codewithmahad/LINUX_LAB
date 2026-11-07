<a id="top"></a>

<h1 id="linux_lab">
  <a href="assets/README.md#tux"><img src="assets/tux.png" align="right" width="18%" alt="Tux, the original Linux penguin by Larry Ewing."></a>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/readme/linux-title-dark.svg">
    <img src="assets/readme/linux-title-light.svg" width="60%" height="44" align="texttop" alt="LINUX_LAB">
  </picture>
</h1>

**Linux commands, Bash scripts, and the notes I come back to.**

I started this repo for my **Operating Systems lab at UBIT, University of Karachi**. I'm working towards **Java and Spring Boot backend development**, and I want the Linux side to feel familiar too: running an application, reading its logs, finding what went wrong, and writing a script when I keep repeating a task.

I keep my attempts here, along with enough explanation to remember what I tried. The map below helps me pick up where I left off.

<p>
  <a href="#current-work">Current work</a> &nbsp;·&nbsp;
  <a href="#learning-map">Learning map</a> &nbsp;·&nbsp;
  <a href="#backend-practice">Backend practice</a> &nbsp;·&nbsp;
  <a href="#working-in-this-lab">Use the lab</a>
</p>

<br clear="right">

<a id="lab-record"></a>

<h2 id="current-work">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/readme/bash-dark.svg">
    <img src="assets/readme/bash-light.svg" align="right" width="14%" alt="GNU Bash logo in grayscale.">
  </picture>
  Current work
</h2>

**Current focus · conditions, loops, and arrays**

The Bash exercises go ahead of my chapter notes. I'm revisiting those attempts before adding arguments and functions.

<br clear="right">

| Area | Work saved | Open it |
| :--- | :--- | :--- |
| Linux commands | 8 chapters, from paths to permissions | [Command notes](learning/linux-commands/) |
| Bash fundamentals | 4 chapters, through operators and exit statuses | [Bash notes](learning/bash-scripting/) |
| Bash practice | 11 scripts across basics, loops, and arrays | [Practice folder](practice/bash-scripting/) |

<details>
<summary><strong>Next session · corrections and the next exercise</strong></summary>

- [ ] Correct the Bash version in the [session audit](practice/bash-scripting/01-basics/02-session-audit.sh), then check its output.
- [ ] Revisit duplicate values in the [second-largest exercise](practice/bash-scripting/04-arrays/03-second-largest.sh) and try invalid input in the early arithmetic scripts.
- [ ] Write short conditions and loops notes from the exercises I've attempted.
- [ ] Turn the [system report](practice/bash-scripting/01-basics/01-system-report.sh) into a script that accepts a project name, practising arguments and functions.

</details>

<a id="what-im-learning"></a>

<h2 id="learning-map">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/readme/filesystem-dark.svg">
    <img src="assets/readme/filesystem-light.svg" align="right" width="20%" alt="Linux filesystem sketch: the root directory branches into home, var, and opt.">
  </picture>
  Learning map
</h2>

The command notes start with files, paths, and permissions. Next I want to get comfortable with processes, ports, application configuration, and working on another Linux machine.

**Recorded** means notes and examples are saved here; **Practising** means exercises exist and need more review; **Next** is still ahead in this lab. I'll update the map as I add work I can run and explain.

<br clear="right">

<details>
<summary><strong>Linux · command notes and the skills to cover next</strong></summary>

The recorded rows link to all eight command chapters. Each row also names a job I expect to use it for.

| Progress | What to learn or revisit | Where I'll use it |
| :--- | :--- | :--- |
| Recorded | **Paths and files:** `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `rm`, `file`, `stat`, `tree`. [Paths](learning/linux-commands/01-navigation-and-paths/README.md) · [Creation](learning/linux-commands/02-files-and-directories/README.md) · [File operations](learning/linux-commands/04-copying-moving-and-deleting/README.md). | Move around projects, inspect files, and organise source, configuration, and build output. |
| Recorded | **Reading and finding:** `cat`, `less`, `head`, `tail`, `grep`, `find`. [Reading files](learning/linux-commands/03-viewing-file-content/README.md) · [Searching](learning/linux-commands/05-searching-and-finding/README.md). | Find a configuration file, follow application logs, and locate the error behind a failed startup. |
| Recorded | **Text processing:** `wc`, `cut`, `sort`, `uniq`, `tr`, basic `sed` and `awk`. [Notes and examples](learning/linux-commands/06-text-processing/README.md). | Filter a log, count repeated errors, and turn command output into a small report. |
| Recorded | **Streams and pipes:** stdin, stdout, stderr, `>`, `>>`, `2>`, `2>&1`, pipes, `tee`. [Notes and examples](learning/linux-commands/07-redirection-and-pipes/README.md). | Save build output, keep diagnostics, and pass results between commands. |
| Recorded | **Basic access:** file and directory `rwx`, `chmod`, ownership, `chown`, `chgrp`, `id`, `umask`. [Permissions notes](learning/linux-commands/08-permissions-and-ownership/README.md). | Understand an access error and choose the permissions a script, config file, or service needs. |
| Next | **Processes and signals:** `ps`, `pgrep`, `top`, `kill`, `jobs`, `fg`, `bg`, `&`; foreground/background work and graceful termination. | Identify the Java process I started, inspect it, and stop it cleanly. |
| Next | **HTTP and networking:** `curl`, `ss`, `ping`, `hostname`, basic DNS lookup; localhost, ports, binding addresses, HTTP status, and timeouts. | Test an endpoint and distinguish an occupied port, a connection failure, and an application error response. |
| Next | **Environment and configuration:** `export`, `printenv`, `PATH`, `JAVA_HOME`, inherited variables, and Spring profiles. | Configure the JDK and application settings for a particular environment; keep real credentials out of Git. |
| Next | **Packages and Java tools:** `apt`, `command -v`, `java -version`, `javac -version`, Maven Wrapper, and `java -jar`. | Prepare Ubuntu for a project, check the selected Java version, and build and run outside the IDE. |
| Next | **Remote work:** `ssh`, keys, host verification, `~/.ssh/config`, `scp`, and basic `rsync`. | Connect to a development VM, transfer a JAR, and investigate a problem on that machine. |
| Next | **Archives and storage:** `tar`, `zip`, `unzip`, `df`, `du`. | Package files, check available space, and find which logs or artifacts are taking it up. |
| Next | **Services and filesystem links:** `systemctl`, `journalctl`, `ln -s`, `readlink`, service users, and when `sudo` is needed. | Inspect a Java service's status and logs, understand its startup configuration, and follow the active release. |

Some later topics already appear in [DeployLatch](#already-applied-deploylatch). I want focused exercises here that I can return to individually.

</details>

<details>
<summary><strong>Bash · fundamentals, practice, and the next scripting skills</strong></summary>

| Progress | What to learn or revisit | Where I'll use it |
| :--- | :--- | :--- |
| Recorded | **Script basics:** shebangs, `bash script.sh`, executable permissions, working directory, and `bash -n`. [Chapter 01](learning/bash-scripting/01-shell-and-script-basics/README.md). | Run a helper script and understand why it behaves differently from an interactive terminal command. |
| Recorded | **Variables and expansion:** assignment, quoting, `${name}`, `$(command)`, integer arithmetic, word splitting, and globbing. [Chapter 02](learning/bash-scripting/02-variables-and-expansion/README.md). | Handle paths and configuration values correctly, including names with spaces. |
| Recorded | **Input and output:** `IFS= read -r`, `printf`, fixed formats, and failed reads. [Chapter 03](learning/bash-scripting/03-input-and-output/README.md). | Read input intact and produce predictable output. |
| Recorded | **Expressions and command results:** numeric and string comparisons, `$?`, `&&`, `\|\|`. [Chapter 04](learning/bash-scripting/04-operators-and-expressions/README.md). | Choose the next action based on a command's result. |
| Practising | **Conditions and loops:** `if`, `case`, `for`, `while`, `break`, `continue`, and validation. [Basics](practice/bash-scripting/01-basics/) · [Loops](practice/bash-scripting/03-loops/). | Validate an argument, retry a check, or repeat a task across files. |
| Practising | **Arrays:** indexed and associative arrays, `"${items[@]}"`, iteration, and duplicate cases. [Array exercises](practice/bash-scripting/04-arrays/). | Keep a list of files or arguments together without losing their boundaries. |
| Next | **Arguments and defaults:** `$1`, `$#`, `"$@"`, `shift`, `${name:-default}`, and usage messages. | Accept a JAR path, environment, or URL without editing the script each time. |
| Next | **Functions and scope:** parameters, `local` variables, return statuses, and separating output from diagnostics. | Reuse validation, logging, and health checks as a script grows. |
| Next | **Failure handling and cleanup:** explicit status checks, `exit`, stderr, `set -e`, `set -u`, `pipefail`, `trap`, and `mktemp`. Learn the limits of each option. | Report a failed build or request, clean up temporary files, and avoid continuing with an invalid result. |
| Next | **Debugging and checks:** `bash -x`, ShellCheck, formatting, and tests for missing input, EOF, spaces, leading zeros, and failed commands. | Find a script's mistake and check the failure paths before relying on it. |

The exercises are grouped into [basics](practice/bash-scripting/01-basics/), [loops](practice/bash-scripting/03-loops/), and [arrays](practice/bash-scripting/04-arrays/). They include reports, a menu calculator, input validation, and array statistics.

</details>

<details>
<summary>How far I want to take it</summary>

My target is to **build, run, and troubleshoot a Java service comfortably on Linux**, and write small Bash scripts I can explain and repair. Looking up an option is fine; I want to know which tool to reach for and what its result tells me.

I'll learn Docker and Compose alongside an application when I'm ready to containerise it. Kernel development, deep system administration, advanced networking, Kubernetes, Terraform, and Ansible can wait until a project or role calls for them. OS-course exercises can still live here; the backend path helps me choose what to practise beyond the lab.

</details>

<a id="learning-resources-and-practice"></a>

<h2 id="backend-practice">
  <a href="https://github.com/codewithmahad/deploylatch">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/readme/deploylatch-dark.svg">
      <img src="assets/readme/deploylatch-light.svg" align="right" width="14%" alt="DeployLatch emblem: a server lock with deployment and recovery arrows.">
    </picture>
  </a>
  Backend practice
</h2>

<a id="already-applied-deploylatch"></a>

**Already applied · [DeployLatch](https://github.com/codewithmahad/deploylatch)**

For my OS course project, I built a Bash tool that deploys one Java service on an Ubuntu VM. It manages versioned JARs, switches the active release through a symbolic link, and checks health and version after restarting the systemd service. I tested both a working update and recovery from a failed one.

The most useful lesson was checking process state, application health, and release identity separately. A running process can still be unhealthy or running the wrong release.

[Deployment script](https://github.com/codewithmahad/deploylatch/blob/main/scripts/deploylatch.sh) · [Update and rollback demo](https://github.com/codewithmahad/deploylatch#deployment-demo)

<br clear="right">

The next tasks are for my Java/Spring Boot projects. I want to practise them alongside the application work and keep a short record of what happened.

<details>
<summary><strong>Six tasks to practise in a Java/Spring Boot project</strong></summary>

I'll check a task off when there's a working example I can repeat.

- [ ] **Run without the IDE.** Build and test with the project's wrapper, select its executable JAR, start it with a profile, and explain the startup output.
- [ ] **Investigate a failed startup.** Find the useful log lines, check the process and listening port, and work out whether the cause is configuration, connectivity, or application code.
- [ ] **Test an API from Bash.** Send requests with `curl`, inspect status and response data, and make a health check return failure when the request or HTTP result fails.
- [ ] **Work on a remote Linux machine.** Connect with SSH, copy an artifact, inspect a service and its journal, and verify the application after a restart.
- [ ] **Automate my development loop.** Write a build/test/run helper with arguments, quoted paths, useful errors, and deliberate handling of failed commands. Reuse the build and test steps in CI.
- [ ] **Archive and restore files.** Back up sample configuration and logs, restore them into a different directory, and verify the restored contents.

</details>

<details>
<summary><strong>Spring Boot commands · build, run, inspect</strong></summary>

These examples belong in a **separate Spring Boot project**. That project needs a configured Maven Wrapper and an executable JAR; `target/app.jar` stands for the actual artifact path.

In the project directory:

```bash
./mvnw verify
SPRING_PROFILES_ACTIVE=dev java -jar target/app.jar
```

While the application is running, use another terminal:

```bash
curl -i --max-time 5 http://localhost:8080/api/users
ss -ltnp 'sport = :8080'
```

The URL must match an endpoint the application exposes. `curl -i` shows response headers as well as the body; this is an inspection command. A scripted check needs an explicit HTTP success condition, such as `curl --fail` for HTTP 400+ responses. `ss` shows listening TCP sockets on port 8080; process details depend on access permissions.

If the application is configured to write `app.log`:

```bash
tail -n 50 -f app.log
```

Spring Boot's [running guide](https://docs.spring.io/spring-boot/reference/using/running-your-application.html) and [configuration reference](https://docs.spring.io/spring-boot/reference/features/external-config.html), the [Maven Wrapper guide](https://maven.apache.org/tools/wrapper/), and the [curl manual](https://curl.se/docs/manpage.html) explain the details.

</details>

<a id="get-a-linux-terminal"></a>
<a id="working-setup"></a>

<h2 id="working-in-this-lab">
  <a href="https://ubuntu.com/"><img src="assets/logos/ubuntu.svg" align="right" width="11%" alt="Ubuntu Circle of Friends."></a>
  Working in this lab
</h2>

**Ubuntu · Bash · Git · VS Code**

I use Ubuntu for the command examples, Bash for scripting, and VS Code with Git for the files and history. Ubuntu in WSL or a VM works for the exercises too.

The [setup guide](docs/GETTING_STARTED.md) covers the terminal, Git, and editor.

<br clear="right">

<a id="lets-run-something"></a>

<details>
<summary><strong>Clone the repo and run the first script</strong></summary>

With Bash and Git available:

```bash
git clone https://github.com/codewithmahad/LINUX_LAB.git
cd LINUX_LAB
bash learning/bash-scripting/01-shell-and-script-basics/hello.sh
```

It prints `Hello From Bash`. Then open a topic in the learning map or try a practice script.

</details>

<details>
<summary><strong>Folders and how I record my practice</strong></summary>

The main folders with recorded work:

```text
LINUX_LAB/
├── learning/
│   ├── linux-commands/       # Command notes and supplied example files
│   └── bash-scripting/       # Bash notes and chapter scripts
├── practice/
│   └── bash-scripting/       # Standalone exercises and attempts
├── docs/                    # Environment setup
├── assets/                  # README and chapter artwork
├── README.md                # Progress, next work, and links
└── LICENSE
```

I'll add automation tools when I have a useful script to keep. Existing chapters stay available for revision; new entries can be a small script and a few notes about the result.

For each topic, I try the example, change something, and explain the result. Before treating a script as finished, I check its normal input and at least one failure case. A mistake and its correction belong here too.

`bash -n path/to/script.sh` checks syntax; `shellcheck path/to/script.sh` helps review common mistakes. I still need to run the script and check what happened. The quoting lesson deliberately includes examples with quotes removed.

</details>

<details>
<summary><strong>References for the next time I forget</strong></summary>

| When I need | Where I'll look |
| :--- | :--- |
| A command's options | Local `man` pages, `command --help` where supported, and `help read` or `help set` for Bash builtins. |
| Bash syntax and behaviour | [GNU Bash manual](https://www.gnu.org/software/bash/manual/) |
| Spring Boot startup and configuration | [Running an application](https://docs.spring.io/spring-boot/reference/using/running-your-application.html) · [External configuration](https://docs.spring.io/spring-boot/reference/features/external-config.html) |
| Building with the project's Maven version | [Apache Maven Wrapper](https://maven.apache.org/tools/wrapper/) |
| HTTP requests and scripted checks | [curl manual](https://curl.se/docs/manpage.html) |
| A service's state and logs | [systemctl](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html) · [journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html) |
| My own applied example | [DeployLatch](https://github.com/codewithmahad/deploylatch) |

</details>

<br>

The other parts of my backend practice: [**Java Lab**](https://github.com/codewithmahad/JAVA_LAB) · [**SQL Lab**](https://github.com/codewithmahad/SQL_LAB) · [**My projects**](https://github.com/codewithmahad?tab=repositories)

If something here helps with your own revision, use it. Found a mistake? [Open an issue](https://github.com/codewithmahad/LINUX_LAB/issues) with the file, command, and result.

<p><sub>Shaikh Mahad · BSSE, UBIT &nbsp;·&nbsp; <a href="LICENSE">MIT License</a> &nbsp;·&nbsp; <a href="assets/README.md">Artwork credits</a> &nbsp;·&nbsp; <a href="#linux_lab">Back to top ↑</a></sub></p>
