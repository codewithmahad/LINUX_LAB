#!/usr/bin/env bash

declare -A prices=(
	[Pen]=50
	[Book]=250
	[Bag]=1500
)

IFS= read -r -p "Enter product: " product || exit 1

if [[ -v prices[$product] ]]; then
	printf 'Price: Rs. %d\n' "${prices[$product]}"
else
	echo "Product not found"
fi
