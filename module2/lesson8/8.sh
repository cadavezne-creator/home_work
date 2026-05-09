#! /bin/bash

# массив с фруктами
fruits=("Холм" "Яблоко" "Груша" "Бобер" "Стол")

# проверяем массив
for fruit in "${fruits[@]}"; do
    echo "$fruit"
done
