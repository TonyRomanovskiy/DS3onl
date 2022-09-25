consum = float(input("Введите расход топлива на на 100 км:"))
consum = consum / 100
road = float(input("Введите длину маршрута:"))

if consum > 0 and road > 0:
    r = road*consum
    r = int(r*100)/100
    print('Вы потратите:',r,'л')
else:
    print("Условия некорректны")


input('Press ENTER to exit')
