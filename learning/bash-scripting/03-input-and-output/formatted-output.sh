#!/usr/bin/env bash

name="Shaikh Mahad"
sessions=3
score=95

printf 'Name: %s\n' "$name"
printf 'Sessions: %d\n' "$sessions"
printf 'Score: %d%%\n' "$score"

# A fixed format keeps percent signs and backslashes in data literal.
note='100% ready for the next script.'
printf '\n%s\n' "$note"
