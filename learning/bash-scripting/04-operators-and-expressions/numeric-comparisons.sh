#!/usr/bin/env bash

first=20
second=15

echo "first = $first"
echo "second = $second"
echo

# Arithmetic comparisons return an exit status.
# 0 means true/success, 1 means false.

(( first > second ))
status=$?
echo "first > second  -> $status"

(( first < second ))
status=$?
echo "first < second  -> $status"

(( first == 20 ))
status=$?
echo "first == 20     -> $status"

(( first != second ))
status=$?
echo "first != second -> $status"

(( first >= second ))
status=$?
echo "first >= second -> $status"