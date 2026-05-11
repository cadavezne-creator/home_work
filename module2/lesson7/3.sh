#! /bin/bash

# Name of the file to check
FILE="8.sh"

# -f checks if the file exists and is a regular file
if [ -f "$FILE" ]; then
    echo "$FILE exists in the current directory."
else
    echo "$FILE does not exist in the current directory."
fi
