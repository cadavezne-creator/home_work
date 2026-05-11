#! /bin/bash

WATCH_DIR="$HOME/watch"

echo "Watching directory: $WATCH_DIR"

while true; do
    # файл без .back
    # -maxdepth 1 — в текущей папке  
    # -type f — только файлы
    find "$WATCH_DIR" -maxdepth 1 -type f -not -name "*.back" | while read -r FILE_PATH; do
        if [ -f "$FILE_PATH" ]; then
            echo "--- New file detected: $(basename "$FILE_PATH") ---"
            cat "$FILE_PATH"
            echo -e "\n----------------------------"
            
            # Переименовываем
            mv "$FILE_PATH" "${FILE_PATH}.back"
        fi
    done
    
    # Пауза в 5 секунд
    sleep 5
done
