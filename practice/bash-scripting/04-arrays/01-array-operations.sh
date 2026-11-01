#!/usr/bin/env bash

items=("Red Pen" "Notebook" "Marker")

items[1]="Large Notebook"
items+=("Eraser")

unset 'items[0]'

printf 'Total: %d\n' "${#items[@]}"

for i in "${!items[@]}"; do
	printf 'Index %d: %s\n' "$i" "${items[i]}"
done
