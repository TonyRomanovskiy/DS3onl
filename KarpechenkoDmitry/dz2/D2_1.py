class MyError(Exception):
    def __init__(self, text):
        self.txt = text
try:
    s = float(input("Введите расстояние, км "))
    r = float(input("Введите расход на 100 км, л "))
    if s < 0 or r<0:
        raise MyError("Введите положительные значение!")
except ValueError:
    print("Введите числовое значение!")
except MyError as mr:
    print(mr)
else:
    print("Расход топлива на", s,"км составляет ", round(r/100*s,1))
