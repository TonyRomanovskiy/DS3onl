# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from array import *
from math import *

def skal_vector(a,b): #объявляем функцию, аргументы -два целочисленных массива
    s1 = 0 #переменная суммы числителя
    s2 = 0 #переменная суммы квадратов значений первого массива
    s3 = 0 #переменная суммы квадратов значений второго массива

    for i in range(len(a)):
        s1 += a[i] * b[i]
        s2 += pow(a[i], 2)
        s3 += pow(b[i], 2)
    return print("Косинусное расстояние векторов", a, " ", b, " ", 1-s1/(sqrt(s2)*sqrt(s3)))
#объявляем целочисленные массивы
a=array("i",[1,1,2])
b=array("i",[1,1,1])
skal_vector(a,b)

