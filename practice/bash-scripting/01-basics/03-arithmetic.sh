#!/usr/bin/env bash

read -r -p "Enter first integer: " a || exit 1
read -r -p "Enter second integer: " b || exit 1

# Limit the size so the multiplication fits in Bash's integer arithmetic.
if [[ ! $a =~ ^-?[0-9]{1,9}$ || ! $b =~ ^-?[0-9]{1,9}$ ]]; then
	printf 'Use integers with up to 9 digits and an optional leading minus.\n' >&2
	exit 1
fi

# Interpret leading zeros as decimal, including negative inputs.
if [[ $a == -* ]]; then
	a=$((-10#${a#-}))
else
	a=$((10#$a))
fi
if [[ $b == -* ]]; then
	b=$((-10#${b#-}))
else
	b=$((10#$b))
fi

echo "Sum: $((a + b))"
echo "Difference: $((a - b))"
echo "Product: $((a * b))"

if ((b == 0)); then
	printf 'Cannot divide by zero.\n' >&2
	exit 1
else
	echo "Quotient: $((a / b))"
	echo "Remainder: $((a % b))"
fi
