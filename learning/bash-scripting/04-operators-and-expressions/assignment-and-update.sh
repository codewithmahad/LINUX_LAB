#!/usr/bin/env bash

count=10

echo "Initial count: $count"

((count++))
echo "After count++: $count"

((count--))
echo "After count--: $count"

((count += 5))
echo "After count += 5: $count"

((count -= 3))
echo "After count -= 3: $count"

((count *= 2))
echo "After count *= 2: $count"

((count /= 4))
echo "After count /= 4: $count"

((count %= 3))
echo "After count %= 3: $count"
