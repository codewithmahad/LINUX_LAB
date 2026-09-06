#!/usr/bin/env bash

read -p "Enter your first number :" first
read -p "Enter your second number :" second

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