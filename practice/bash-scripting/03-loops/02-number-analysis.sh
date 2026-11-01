#!/usr/bin/env bash

while true; do
	read -r -p "Enter n (1-100): " input || exit 1

	if [[ $input =~ ^[0-9]{1,3}$ ]]; then
		n=$((10#$input))

		if ((n >= 1 && n <= 100)); then
			break
		fi
	fi

	echo "Invalid number."
done

sum=0
count=0
even_count=0

printf 'Accepted numbers: '

for ((i = 1; i <= n; i++)); do
	if ((i % 3 == 0)); then
		continue
	fi

	printf '%d ' "$i"

	sum=$((sum + i))
	count=$((count + 1))

	if ((i % 2 == 0)); then
		even_count=$((even_count + 1))
	fi
done

printf '\nSum: %d\n' "$sum"
printf 'Count: %d\n' "$count"
printf 'Even accepted numbers: %d\n' "$even_count"
