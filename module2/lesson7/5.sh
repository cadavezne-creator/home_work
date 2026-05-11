#! /bin/bash

# check filename and path
if [ "$#" -ne 2 ]; then
    echo "Использование: $0 <откуда> <куда>"
    exit 1
fi

SOURCE=$1
DEST=$2

cp "$SOURCE" "$DEST"

# check copy good/ bad
if [ $? -eq 0 ]; then
    echo "copy file good $DEST"
else
    echo "copy file bad"
fi
