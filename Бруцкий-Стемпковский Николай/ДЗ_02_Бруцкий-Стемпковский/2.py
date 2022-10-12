"""
08092022
Бруцкий-Стемпковский
v.01

ex_2. Задача нахождения действительных корней квадратного уравнения
"""
from decimal import DivisionByZero


print("Введите коэффициенты квадратного уравнения")
a = float(input())
b = float(input())
c = float(input())

def solver(a,b,c):

    import math

    Disc = b**2 - 4*a*c
    try:
        if Disc < 0:
            return "Действительных корней нет"
        elif Disc == 0:
            return -b/(2*a)
        else:
            return (-b-math.sqrt(Disc))/(2*a), (-b+math.sqrt(Disc))/(2*a)
    except ZeroDivisionError:
        return("Деление на ноль, введите нормальное уравнение")

print(solver(a, b, c))
