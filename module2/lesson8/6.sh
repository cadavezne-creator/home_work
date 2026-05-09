x#! /bin/bash

# ввести предложение
echo "Введите что нибудь из нескольких слов:"
read -r sentence

# загоняем предложение в массив
read -ra words <<< "$sentence"

# Переворачиваем порядок слов
reversed=""
for (( i=${#words[@]}-1; i>=0; i-- )); do
    reversed="$reversed ${words[i]}"
done

# Выводим результат
echo "Результат:${reversed}"
