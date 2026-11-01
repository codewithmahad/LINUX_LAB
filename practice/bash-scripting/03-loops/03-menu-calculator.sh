#!/usr/bin/env bash

while true; do
	printf '\n========== CALCULATOR ==========\n'
	echo "1. Addition"
	echo "2. Subtraction"
	echo "3. Multiplication"
	echo "4. Division"
	echo "5. Exit"

	read -r -p "Enter choice: " choice || exit 1

	case "$choice" in
	1 | 2 | 3 | 4)
		read -r -p "First number: " a || exit 1
		read -r -p "Second number: " b || exit 1

		if [[ ! $a =~ ^[0-9]{1,3}$ || ! $b =~ ^[0-9]{1,3}$ ]]; then
			echo "Invalid integers."
			continue
		fi

		a=$((10#$a))
		b=$((10#$b))

		case "$choice" in
		1)
			result=$((a + b))
			;;
		2)
			result=$((a - b))
			;;
		3)
			result=$((a * b))
			;;
		4)
			if ((b == 0)); then
				echo "Cannot divide by zero."
				continue
			fi
			result=$((a / b))
			;;
		esac

		printf 'Result: %d\n' "$result"
		;;
	5)
		echo "Goodbye."
		break
		;;
	*)
		echo "Invalid choice."
		;;
	esac
done
