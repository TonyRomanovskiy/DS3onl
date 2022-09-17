from math import pow
max=-10000
min=0
x=-5
while x<=5.1:
    y=-26*pow(x,2)+25*x-9
    if max<y:
        max=y
    if min>y:
        min=y
    x+=0.1
print("min(y)=",round(min,1),"max(y)=",round(max,1))