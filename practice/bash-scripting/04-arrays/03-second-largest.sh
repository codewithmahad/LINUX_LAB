#!/bin/bash
numbers=(-10 -3 -7 -3)

max=""
second_max=""
for num in "${numbers[@]}"; do

	if [[ -z "$max" ]]; then
		max=$num
	elif [[ $num -gt $max ]]; then
		second_max=$max
		max=$num
	elif [[ -z $second_max || $num -gt $second_max && $num -ne $max ]]; then
		second_max=$num
	fi
done
echo "the second largest number is: $second_max"]]
