#! /bin/bash

#  Генерация числа 
target=$((RANDOM % 100 + 1))
attempts=5

echo "Вгадай число. У вас $attempts спроб"

for (( i=1; i<=attempts; i++ )); do
    read -p "Спроба $i: Введіть ваше число: " guess

    if [[ $guess -eq $target ]]; then
        echo "Красунчик! Вгадав число."
        exit 0
    elif [[ $guess -lt $target ]]; then
        echo "Вишче."
    else
        echo "Нижче"
    fi
done

echo "Закінчилися спроби. А там було $target."
