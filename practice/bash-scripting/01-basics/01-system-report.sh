#!/usr/bin/env bash

read -r -p "Enter project name: " project

current_user=$(whoami)
machine_name=$(hostname)
current_directory=$(pwd)
timestamp=$(date '+%F %T')

printf '\nSYSTEM SESSION REPORT\n'
printf 'Project   : %s\n' "$project"
printf 'User      : %s\n' "$current_user"
printf 'Machine   : %s\n' "$machine_name"
printf 'Directory : %s\n' "$current_directory"
printf 'Timestamp : %s\n' "$timestamp"


