#!/usr/bin/env bash

# Read two labels and report the shell and system running this session.
IFS= read -r -p "Enter the application name: " app_name || exit 1
IFS= read -r -p "Enter the environment name: " env_name || exit 1
current_user=$(whoami)
os_name=$(uname -s)
current_date_time=$(date '+%F %T')

printf '\nSESSION AUDIT REPORT\n'
printf 'Application Name      : %s\n' "$app_name"
printf 'Environment Name      : %s\n' "$env_name"
printf 'Current User          : %s\n' "$current_user"
printf 'Operating System Name : %s\n' "$os_name"
printf 'Bash Version          : %s\n' "$BASH_VERSION"
printf 'Current Date/Time     : %s\n' "$current_date_time"
