"""
08092022
Бруцкий-Стемпковский
v.01

ex_3. Задача нахождения min/max значения заданной функции на отрезке [-5; 5] с задаваемым шагом
"""
def func(x):
    return 26*x**2 + 25*x - 9

def solver():
    start_x, finish_x = -5, 5
    cur_x = start_x
    min_, max_ = float("inf"), -float("inf")
    step = 0.1
    while cur_x <= finish_x:
        y = func(cur_x)
        min_=min(min_, y)
        max_=max(max_,y)
        cur_x += step
    return min_, max_

print("min/max на интервале [-5; 5]")
print(solver())