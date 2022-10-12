# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from array import *

def skal_vector(a,b):
    s=0
    for i in range(len(a)):
        s+=a[i]*b[i]
    return print(a,' ',b,' ',s)

#объявляем два целочисленных массива-вектора
a=array('i',[1,1,2])
b=array('i',[1,1,3])
skal_vector(a,b)


