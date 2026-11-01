#!/bin/bash

read -r -p "Enter first number: " a
read -r -p "Enter second number: " b

echo "Sum: $((a + b))"
echo "Difference: $((a - b))"
echo "Product: $((a * b))"

if ((b == 0)); then
	echo "Cannot divide by zero"
else
	echo "Quotient: $((a / b))"
	echo "Remainder: $((a % b))"
fi
