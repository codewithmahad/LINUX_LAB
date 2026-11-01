#!/usr/bin/env bash

marks=(72 45 90 33 50)

total=0
passed=0
minimum=${marks[0]}
maximum=${marks[0]}

for mark in "${marks[@]}"; do
	total=$((total + mark))

	if ((mark > maximum)); then
		maximum=$mark
	fi

	if ((mark < minimum)); then
		minimum=$mark
	fi

	if ((mark >= 50)); then
		passed=$((passed + 1))
	fi
done

count=${#marks[@]}
failed=$((count - passed))
average=$((total / count))

printf 'Total: %d\n' "$total"
printf 'Average: %d\n' "$average"
printf 'Maximum: %d\n' "$maximum"
printf 'Minimum: %d\n' "$minimum"
printf 'Passed: %d\n' "$passed"
printf 'Failed: %d\n' "$failed"
