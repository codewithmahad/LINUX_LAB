#!/usr/bin/env bash

# Variables are created through assignment.
name="Mahad"
course="Operating Systems"
semester=4

echo "Name: $name"
echo "Course: $course"
echo "Semester: $semester"

# Empty variable
empty_value=""
echo "Empty value: '$empty_value'"

# Arithmetic context
number=10
result=$((number + 5))

echo "Number: $number"
echo "Result: $result"

# A variable can also be declared explicitly.
declare declared_later
declared_later="Assigned later"

echo "$declared_later"