'''Карпеченко Дмитрий, DZ05, 2022/09/24, v.0.1'''
import string

#Создаю класс Alphabet. Определяем метод  __init__ с двумя параметрами.
# Так же определяю значения параметров по умолчанию
class Alphabet:
    def __init__(self, *args, **kwargs):
            self.lang = args[0] if len(args)>0 else 'RU'
            self.let = args[1] if len(args)>1 else 'щщщщщ'

#Создаю метод print, который выводит все буквы алфавита
    def print(self):
        print(self.let)

# Создаю метод letters_num, который выводит количество букв
    def letters_num(self):
        print(len(self.let))

#Создаю класс EngAlphabet, который наследуется от класса Alphabet.
# Определяем метод  __init__ , который вызывает метод __init__ родительского класса и задаю значения переменным.
class EngAlphabet(Alphabet):

    def __init__(self, *args, **kwargs):
        super().__init__('EN', string.ascii_lowercase)

# Создаю приватный метод __letters_num, который выводит количество букв алфавита.
    def __letters_num(self):
        return len(self.let)

# Создаю метод is_en_letter, который на вход принимает букву и определяет буква английского алфавита или нет.
    def is_en_letter(self, let1):
        self.let1=let1
        if let1 in string.ascii_lowercase or let1 in string.ascii_uppercase:
            print('Буква английского алфавита!')
        else:
            print('Буква не английского алфавита!')

# Переопределяю метод letters_num
    def letters_num(self):
        super().letters_num()

# Создаю статический метод example, выводящий строку на английском языке
    @staticmethod
    def example():
        print("This is example in english")

#1. Создайте объект класса EngAlphabet
a=EngAlphabet()
print(a)
#2. Напечатайте буквы алфавита для этого объекта
a.print()
#3. Выведите количество букв в алфавите
a.letters_num()
#4. Проверьте, относится ли буква F к английскому алфавиту
a.is_en_letter('F')
#5. Проверьте, относится ли буква Щ к английскому алфавиту
a.is_en_letter('Щ')
#6. Выведите пример текста на английском языке
a.example()
