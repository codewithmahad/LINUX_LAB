#!/usr/bin/env bash

# Variables are created through assignment.
name="Shaikh Mahad"
course="Operating Systems"
topic="Bash"

echo "Name: $name"
echo "Course: $course"
echo "Topic: $topic"

# Braces separate the variable name from the text after it.
notebook="${topic}_notes"
echo "Notebook: $notebook"

# Assignment can replace a value without declaring its type.
topic="Bash scripting"
echo "Updated topic: $topic"

# Empty is a value; unset removes the variable.
optional_note=""
echo "Empty note: <$optional_note>"
unset optional_note
