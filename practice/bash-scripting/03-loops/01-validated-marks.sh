#!/usr/bin/env bash

while true; do
	read -r -p "Enter marks (0-100): " marks || exit 1

	# Step 1: Check the input format
	if [[ $marks =~ ^[0-9]{1,3}$ ]]; then
		# Step 2: Interpret the digits as decimal
		marks=$((10#$marks))

		# Step 3: Check the allowed range
		if ((marks <= 100)); then
			break
		fi
	fi

	echo "Invalid marks. Try again."
done

# Determine the final result
if ((marks >= 40)); then
	echo "PASS"
else
	echo "FAIL"
fi
