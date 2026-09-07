#!/usr/bin/env bash

role="student"
active="no"

# This student is not active, so only the first test is false.

[[ "$role" == "student" && "$active" == "yes" ]]
status=$?
echo "student AND active -> $status"

[[ "$role" == "admin" || "$role" == "student" ]]
status=$?
echo "admin OR student   -> $status"

[[ ! "$role" == "admin" ]]
status=$?
echo "NOT admin          -> $status"
