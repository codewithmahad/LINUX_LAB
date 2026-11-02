# Getting started with LINUX_LAB

Set up a Linux terminal, install Git, and configure your editor. Already have Bash and Git? [Run the first script in the README](../README.md#lets-run-something), or jump to [editor setup](#a-comfortable-place-to-practise).

[Terminal setup](#get-a-linux-terminal) · [Install Git](#install-git) · [Editor setup](#a-comfortable-place-to-practise)

[Back to the learning map](../README.md#what-im-learning)

<a href="https://ubuntu.com/desktop"><img align="right" src="../assets/logos/ubuntu.svg" alt="Ubuntu Circle of Friends logo." width="120"></a>

## Get a Linux terminal

You can keep your current operating system. Pick the setup that fits what you want to try. The steps below use Ubuntu, so we have a common starting point for commands, package names, and examples.

<br clear="right">

### Ubuntu in WSL

These steps are for **Windows 11**, or **Windows 10 version 2004 / build 19041 or later**.

1. Open **PowerShell as administrator**. Run:

   ```powershell
   wsl --install -d Ubuntu
   ```

2. Restart when prompted, then open **Ubuntu** from the Start menu.
3. Create your Linux username and password. Nothing appears while you type the password, even dots. That's normal.
4. In the Ubuntu terminal, check Bash:

   ```bash
   bash --version
   ```

Run this repo's Linux commands in that Ubuntu terminal. The PowerShell command above is just for setting it up.

If installation needs troubleshooting, Microsoft's [WSL installation guide](https://learn.microsoft.com/en-us/windows/wsl/install) and [first-time setup guide](https://learn.microsoft.com/en-us/windows/wsl/setup/environment) cover the details.

### Ubuntu in a virtual machine

A virtual machine lets you explore Ubuntu while your usual operating system is still running.

1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads). If your lab uses VMware, [Workstation or Fusion](https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion) is another option.
2. Download **Ubuntu Desktop LTS** from [Ubuntu's download page](https://ubuntu.com/download/desktop). LTS means *long-term support*. Choose the image for your computer: Intel/AMD 64-bit for Intel/AMD machines, or ARM64 for an Apple Silicon VM.
3. Create a new VM and select the downloaded ISO as its installation image. Allocate memory and virtual disk space using Ubuntu's listed requirements, leaving enough memory for your main OS. In VirtualBox's creation wizard, choose **Skip Unattended Installation** if that option appears and you want to go through the installer yourself.
4. Start the VM and follow Ubuntu's installer.
5. Create your account, finish the installation, and restart the VM when asked. Open Ubuntu's **Terminal** app and run:

   ```bash
   bash --version
   ```

Do the installation **inside the VM window**; its virtual disk is where Ubuntu goes.

Ubuntu's [VirtualBox walkthrough](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox) shows the screens. Use a VM application and Ubuntu image that both support your computer's architecture.

**Terminal ready?** Check Git below, then [clone the repo and run your first script](../README.md#lets-run-something).

## Install Git

Inside your Linux terminal, check that Git is available with `git --version`. If Ubuntu says the command is missing, install it:

```bash
sudo apt update
sudo apt install git
```

`sudo` asks for your Linux password. Nothing appears while you type it, even dots. That's normal.

Continue with [the README's first-run commands](../README.md#lets-run-something). The [practice section](../README.md#learning-resources-and-practice) has exercises and lab reminders once you're ready.

<a href="https://code.visualstudio.com/"><img align="right" src="../assets/logos/vscode.svg" alt="Visual Studio Code logo." width="125"></a>

## A comfortable place to practise

Use an editor you already like. If that's **VS Code**, a useful layout is the chapter notes beside your script, with a terminal underneath. Read a little, edit a little, run it, and keep the result in view.

Open the cloned `LINUX_LAB` folder. From **Terminal → New Terminal**, choose a Bash terminal. On Windows with WSL, open the project through the **WSL extension** so the commands run in Ubuntu.

The [VS Code terminal guide](https://code.visualstudio.com/docs/terminal/basics) and [WSL walkthrough](https://code.visualstudio.com/docs/remote/wsl) show how to set that up. The examples here also work in a separate Ubuntu terminal if you prefer.

<br clear="right">

[Back to the learning map](../README.md#what-im-learning)
