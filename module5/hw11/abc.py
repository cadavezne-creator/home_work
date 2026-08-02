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
    
    