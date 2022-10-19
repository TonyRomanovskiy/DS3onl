print('Введите коэффициенты вашего квадратного уравнения')
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

print("Ваше уравнение:")
print(a,'*x*x+',b,'*x+',c,'=0')

d= b*b-4*a*c
print('D=',d)

if d > 0:
    x1 = (-b+d**(0.5))/(2*a)
    x2 = (-b-d**(0.5))/(2*a)
    x1 =int(x1*100)/100
    x2 =int(x2*100)/100
    print('В уравнении 2 корня:',x1,'и',x2)
elif d == 0:
    x=-b/(2*a)
    print('В уравнении один корень =',x)
else:
    print('В уравнение нет корней')

input('Press ENTER to exit')
