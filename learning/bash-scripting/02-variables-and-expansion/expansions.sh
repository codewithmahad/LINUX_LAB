#!/usr/bin/env bash

name="Shaikh Mahad"
sessions=3

# Parameter expansion
echo "Student: ${name}"

# Command substitution
current_directory="$(pwd)"
echo "Current directory: $current_directory"

# Arithmetic expansion
next_session=$((sessions + 1))
echo "Next session: $next_session"

# An unquoted tilde expands. A quoted tilde stays literal.
echo ~
echo "~"
echo "$HOME"
