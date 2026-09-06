#!/usr/bin/env bash

age=20
role="student"
active="yes"

[[ "$role" == "student" && "$active" == "yes" ]]
status=$?
echo "student AND active -> $status"

[[ "$role" == "admin" || "$role" == "student" ]]
status=$?
echo "admin OR student   -> $status"

[[ ! "$role" == "admin" ]]
status=$?
echo "NOT admin          -> $status"