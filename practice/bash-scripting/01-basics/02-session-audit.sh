#!/bin/bash


# Write a script that asks for an application name and environment name, then prints a formatted audit report containing the application, environment, current user, operating-system name, Bash version and current date/time.

# Use the Linux command uname -s for the operating-system/kernel name and the Bash variable $BASH_VERSION for the interpreter version.

read -rp "Enter the application name: " app_name
read -rp "Enter the environment name: " env_name
current_user=$(whoami)
os_name=$(uname -s)
bash_version=$(Bash_Version)
current_date_time=$(date '+%F %T')

echo "============Session Audit Report============="
echo "Application Name      : $app_name"
echo "Environment Name      : $env_name"
echo "Current User          : $current_user"
echo "Operating System Name : $os_name"
echo "Current Date/Time     : $current_date_time"