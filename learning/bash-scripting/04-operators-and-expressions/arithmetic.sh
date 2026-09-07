#!/usr/bin/env bash

# Fixed values keep this example about operators. Input is in chapter 03.
# Use integers here and keep second nonzero for division and remainder.
first=17
second=5

sum=$((first + second))
difference=$((first - second))
product=$((first * second))
quotient=$((first / second))
remainder=$((first % second))

echo "First number: $first"
echo "Second number: $second"
echo

echo "Sum: $sum"
echo "Difference: $difference"
echo "Product: $product"
echo "Quotient: $quotient"
echo "Remainder: $remainder"
echo "2 ** 8: $((2 ** 8))"

# Multiplication happens first unless parentheses change the order.
echo "2 + 3 * 4: $((2 + 3 * 4))"
echo "(2 + 3) * 4: $(((2 + 3) * 4))"
