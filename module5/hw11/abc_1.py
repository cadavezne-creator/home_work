class Uaalphabet:
# создали класс uaalphabet
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self): 
        # Вівели букви та мову     
        print(f"Language: {self.lang}")
        print(f"Letters: {self.letters}")

    def letters_num(self): 
        # Вивели кількість букв
        return len(self.letters)    




# Заполняем класс данніми и буквами
Uaalphabet = Uaalphabet("Українська", ["А", "Б", "В", "Г", "Д", "Е", "Є", "Ж", "З", "И", "І", "Ї", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ь", "Ю", "Я"])


# Тестируем - віводим мову
print(Uaalphabet.lang)

# Тестируем - віводим букви
print(Uaalphabet.letters)

# Тестируем - сщздаем переменную и говорим что она равна методу letters_num
letters_count = Uaalphabet.letters_num()
print(f"Всього букв: {letters_count}")

