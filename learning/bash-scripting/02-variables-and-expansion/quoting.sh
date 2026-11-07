#!/usr/bin/env bash

name="Shaikh Mahad"

echo "Hello, $name"
# This line deliberately keeps the variable name literal.
# shellcheck disable=SC2016
echo 'Hello, $name'

message="Linux and Bash"

# %s prints one argument; \n ends the line. < > are just visible markers.
echo "Without quotes:"
# Deliberately unquoted to demonstrate word splitting.
# shellcheck disable=SC2086
printf '<%s>\n' $message

echo "With double quotes:"
printf '<%s>\n' "$message"
