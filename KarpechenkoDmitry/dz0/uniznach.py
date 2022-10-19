from array import *

#бъявляем функцию
def uni(a):
    for i in range(len(a)):
        if a.count(a[i])==1: #если количество текущего значения во всем массиве 1, то выводим его
            print(a[i])

a=array("i",[1,1,2,1,0,4,4,7])
uni(a)