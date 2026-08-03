class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def letters_num(self):
        return len(self.letters)

    def is_alphabet_letter(self, letters, letter):
        return "О, так" if letter.lower() in letters else "О, ніт!!!"

class UaAlphabet(Alphabet):
    def __init__(self):
        super().__init__("Українська", list("абвгдеєжзиіїйклмнопрстуфхцчшщьюя"))

    def is_ua_letter(self, letter):
        return self.is_alphabet_letter(self.letters, letter)

class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__("English", list("abcdefghijklmnopqrstuvwxyz"))

    def is_en_letter(self, letter):
        return self.is_alphabet_letter(self.letters, letter)

    @staticmethod
    def example():
        return "The quick brown fox jumps over the lazy dog."

# Заполняем класс данніми и буквами
uaAlphabet = UaAlphabet()

# Заполняем класс данніми и буквами
engAlphabet = EngAlphabet()

# Тестируем - віводим мову
print(uaAlphabet.lang)

# Тестируем - віводим букви
print(uaAlphabet.letters)

# Тестируем - сщздаем переменную и говорим что она равна методу letters_num
letters_count = uaAlphabet.letters_num()
print(f"Всього букв: {letters_count}")

# Тестируем - віводим мову
print(engAlphabet.lang)

# Тестируем - віводим букви
print(engAlphabet.letters)

# Тестируем - сщздаем переменную и говорим что она равна методу letters_num
letters_count = engAlphabet.letters_num()
print(f"Всього букв: {letters_count}")

# Перевіряємо, чи належить літера  англійському алфавіту
# while(True):
name = input("Введіть англійську літеру: ")
print(engAlphabet.is_en_letter(name))

# Перевіряємо, чи належить літера  українському алфавіту
# while(True):
name = input("Введіть українську літеру: ")
print(uaAlphabet.is_ua_letter(name))