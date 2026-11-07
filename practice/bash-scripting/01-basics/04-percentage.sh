#!/usr/bin/env bash

# Write a program that:
# - Accepts obtained marks for three subjects, each out of 100.
# - Calculates total obtained marks out of 300.
# - Calculates the percentage using Bash integer arithmetic.
# - Displays the total, percentage and whether the percentage is at least 50.
# - Rejects marks outside 0-100 and input that is not a whole number.

read -r -p "Subject 1: " a || exit 1
read -r -p "Subject 2: " b || exit 1
read -r -p "Subject 3: " c || exit 1

if [[ ! $a =~ ^[0-9]{1,3}$ || ! $b =~ ^[0-9]{1,3}$ || ! $c =~ ^[0-9]{1,3}$ ]]; then
	printf 'Each mark must be a whole number from 0 to 100.\n' >&2
	exit 1
fi

a=$((10#$a))
b=$((10#$b))
c=$((10#$c))
if ((a > 100 || b > 100 || c > 100)); then
	printf 'Each mark must be a whole number from 0 to 100.\n' >&2
	exit 1
fi

total=$((a + b + c))
percentage=$((total * 100 / 300))

echo "Total: $total/300"
echo "Percentage: $percentage%"

if ((percentage >= 50)); then
	echo "PASS"
else
	echo "FAIL"
fi
