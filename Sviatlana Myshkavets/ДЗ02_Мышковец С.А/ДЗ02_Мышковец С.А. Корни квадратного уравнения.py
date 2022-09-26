import math


def roots(a, b, c):
    """"
    Вычисляет корни квадратного уравнения вида a*x*x+b*x+c. На вход подаются a,b,c.
    Результат функции – действительные корни или сообщение, что корней нет.
    """
    d = b**2 - 4*a*c
    if d < 0:
        return f'Корней нет.'
    if d == 0:
        d1 = math.sqrt(d)
        x = (-1 * b + d1) / 2 * a
        return f'x={x}'
    else:
        d1 = math.sqrt(d)
        x1 = (-1*b + d1) / 2*a
        x2 = (-1*b - d1) / 2*a
        return f'x1={round(x1, 4)}, x2={round(x2, 4)}'


print(roots(-2, -3, 4))
