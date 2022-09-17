from math import *
a,b,c=float(input()),float(input()),float(input())
d=b*b-4*a*c
if d<0:
    print("Нет корней")
elif d==0:
    print(b*(-1)/(2*a))
elif d>0:
    x1=(b*(-1)-sqrt(d))/(2*a)
    x2=(b*(-1)+sqrt(d))/(2*a)
    print(x1," ",x2)
