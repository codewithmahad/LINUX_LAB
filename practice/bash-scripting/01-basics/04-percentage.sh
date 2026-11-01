#!/bin/bash

# Write a program that:
# - Accepts obtained marks for three subjects, each out of 100.
# - Calculates total obtained marks out of 300.
# - Calculates the percentage using Bash integer arithmetic.
# - Displays the total, percentage and whether the percentage is at least 50.
# - Rejects division by zero if you extend it to a user-provided maximum mark.

read -r -p "Subject 1: " a
read -r -p "Subject 2: " b
read -r -p "Subject 3: " c

total=$((a + b + c))
percentage=$((total * 100 / 300))

echo "Total: $total/300"
echo "Percentage: $percentage%"

if ((percentage >= 50)); then
	echo "PASS"
else
	echo "FAIL"
fi
