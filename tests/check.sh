#!/usr/bin/env bash

# Run the same checks locally and in GitHub Actions.
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1

for tool in shellcheck python3; do
	if ! command -v "$tool" >/dev/null 2>&1; then
		printf 'Missing check dependency: %s\n' "$tool" >&2
		exit 1
	fi
done

mapfile -d '' -t scripts < <(find learning practice tests -type f -name '*.sh' -print0)
for script in "${scripts[@]}"; do
	bash -n "$script" || exit 1
done
printf 'Syntax checked: %s Bash scripts\n' "${#scripts[@]}"

shellcheck "${scripts[@]}" || exit 1
printf 'ShellCheck passed.\n'
python3 -m unittest discover -s tests -p 'test_*.py' -v
