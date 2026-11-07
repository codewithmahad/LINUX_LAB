#!/usr/bin/env bash

# Collect three complete names, then print them without changing their text.
names=()

for ((i = 0; i < 3; i++)); do
	IFS= read -r -p "Enter name: " name || exit 1
	names+=("$name")
done

printf 'Total names: %d\n' "${#names[@]}"

for name in "${names[@]}"; do
	printf '%s\n' "$name"
done
