#!/usr/bin/env bash

# true returns 0; false returns 1. Neither prints anything itself.
true && echo "Success: the command after && ran."
false && echo "You will not see this line."
false || echo "Failure: the fallback after || ran."
true || echo "You will not see this line either."

# The same rule works with a comparison. No files are created here.
topic="Bash"

[[ -n "$topic" ]] && echo "Topic: $topic"

[[ "$topic" == "Python" ]] || echo "Still working on Bash."
