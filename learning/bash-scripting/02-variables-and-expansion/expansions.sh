#!/usr/bin/env bash

name="Mahad"
year=2026

# Parameter expansion
echo "Student: ${name}"

# Command substitution
current_directory="$(pwd)"
echo "Current directory: $current_directory"

echo "Current directory: $(pwd)"

# Arithmetic expansion
next_year=$((year + 1))
echo "Next year: $next_year"

# Tilde expansion
echo "Home directory:"
echo ~