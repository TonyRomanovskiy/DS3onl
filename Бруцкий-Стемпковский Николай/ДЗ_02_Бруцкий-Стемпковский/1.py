"""
08092022
Бруцкий-Стемпковский
v.01

ex_1. Задача нахождения расхода топлива
"""
print("Введите длину маршрута, км")
length = float(input())
print("Введите удельный расход топлива, л/100 км")
consumption = float(input())

def sum_consumption(length, consumption):

    try:
        1/length
    except:
        print("Мы нисколько не проехали...")
        return("")
    
    try:
        1/consumption
    except:
        print("У нас нулевой удельный расход...")
        return("")
    
    sum_consumption = length*consumption/100
    print("Суммарный расход {} л".format(sum_consumption))

sum_consumption(length, consumption)
    


