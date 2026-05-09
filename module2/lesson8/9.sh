#! /bin/bash

# путь к файлу 
FILE_PATH="3.sh"

# есть ли файл и можем ли читать
if [[ -f "$FILE_PATH" && -r "$FILE_PATH" ]]; then
    echo "--- Содержимое файла $FILE_PATH ---"
    cat "$FILE_PATH"
else
    echo "Файл '$FILE_PATH' не найден или недоступен для чтения."
    exit 1
fi
