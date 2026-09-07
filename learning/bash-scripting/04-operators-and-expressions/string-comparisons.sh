#!/usr/bin/env bash

username="mahad"
role="student"
empty_value=""

[[ "$username" == "mahad" ]]
status=$?
echo 'username == "mahad" ->' "$status"

[[ "$role" != "admin" ]]
status=$?
echo 'role != "admin"      ->' "$status"

[[ -n "$username" ]]
status=$?
echo 'username is non-empty ->' "$status"

[[ -z "$empty_value" ]]
status=$?
echo 'empty_value is empty  ->' "$status"

# Quoted text is literal; an unquoted * on the right is a pattern.
filename="notes.sh"

[[ "$filename" == "*.sh" ]]
status=$?
echo 'filename == "*.sh" (literal) ->' "$status"

[[ "$filename" == *.sh ]]
status=$?
echo 'filename == *.sh (pattern)   ->' "$status"
