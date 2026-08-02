import random

def guess_the_number():
    # Генерація числа від 1 до 100
    secret_number = random.randint(1, 100)
    attempts_limit = 5
    
    print("Я загадав від 1 до 100. Вгадай !")
    
    # Цикл для обмеженої кількості спроб    
    for attempt in range(1, attempts_limit + 1):
        # Отримання даних юзера та обробка помилок введення
        try:
            user_guess = int(input(f"Спроба {attempt}/{attempts_limit}. Введіть число: "))
        except ValueError:
            print("Будь ласка, введіть ціле число.")
            continue

        # Перевірка результату
        if user_guess == secret_number:
            print(" Ви вгадали правильне число.")
            return  # Вихід з функції та завершення програми
        elif user_guess > secret_number:
            print("Ти богато хочешь")
        else:
            print("Мені потрібно більше золотa")
            
    # Якщо 5 спроб вичерпано
    print(f"\nВибачте, у вас закінчилися спроби. Правильний номер був {secret_number}")

# Виклик функції для запуску гри
guess_the_number()
