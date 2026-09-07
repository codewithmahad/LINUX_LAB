#!/usr/bin/env bash

# Keep spaces and backslashes. Stop if a complete line cannot be read.
# || runs exit 1 only if read fails; exit 1 ends the script with failure status.
IFS= read -r -p "Enter your name: " name || exit 1
IFS= read -r -p "Enter your course: " course || exit 1

printf '\nStudent information\n'
printf 'Name: %s\n' "$name"
printf 'Course: %s\n' "$course"
