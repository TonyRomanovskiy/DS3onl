
print('Ваша фукция: y = -26*x**2+25*x-9')

x = -5
y = -26*x*x+25*x-9

while x <= 5:
    a = -26*x*x+25*x-9
    x = x+0.1
    a = int(a*100)/100
    print(a)
    if a > y:
        y = a

print('Наибольшее значение фукции',y)

input('Press ENTER to exit')

