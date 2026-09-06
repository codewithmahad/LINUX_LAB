#!/usr/bin/env bash

echo "Running first command" && echo "First command succeeded"

mkdir -p demo-directory && echo "Directory is ready"

ls demo-directory && echo "Directory can be accessed"

ls missing-directory || echo "Could not access missing-directory"