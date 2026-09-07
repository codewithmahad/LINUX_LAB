#!/usr/bin/env bash

name="Shaikh Mahad"

echo "Hello, $name"
echo 'Hello, $name'

message="Linux and Bash"

# %s prints one argument; \n ends the line. < > are just visible markers.
echo "Without quotes:"
# Deliberately unquoted to demonstrate word splitting.
printf '<%s>\n' $message

echo "With double quotes:"
printf '<%s>\n' "$message"
