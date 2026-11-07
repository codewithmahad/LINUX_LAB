#!/usr/bin/env bash

# Use the sample array by default, or try integers passed as arguments.
numbers=(-10 -3 -7 -3)
if (($# > 0)); then
	numbers=("$@")
fi

max=""
second_max=""
for num in "${numbers[@]}"; do
	if [[ ! $num =~ ^-?[0-9]{1,9}$ ]]; then
		printf 'Use integers with up to 9 digits and an optional leading minus.\n' >&2
		exit 1
	fi
	if [[ $num == -* ]]; then
		num=$((-10#${num#-}))
	else
		num=$((10#$num))
	fi

	if [[ -z "$max" ]]; then
		max=$num
	elif ((num > max)); then
		second_max=$max
		max=$num
	elif ((num < max)); then
		if [[ -z $second_max ]] || ((num > second_max)); then
			second_max=$num
		fi
	fi
done

if [[ -z $second_max ]]; then
	printf 'Need at least two distinct integers.\n' >&2
	exit 1
fi
printf 'Second largest distinct number: %s\n' "$second_max"
