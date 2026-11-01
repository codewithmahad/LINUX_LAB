#!/usr/bin/env bash

marks=(75 82 91 68 88)

names=()

for ((i = 0; i < 3; i++)); do
	read -r -p "Enter name: " name || exit 1
	names+=("$name")
done

printf 'Total names: %d\n' "${#names[@]}"

for name in "${names[@]}"; do
	echo "$name"
done
