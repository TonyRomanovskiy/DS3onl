# Напишите функцию, которая на вход принимает два вектора и возвращает скалярное произведение данных векторов.

import math
import numpy as np

# Функция получения скалярное произведения векторов
def getDotProduct(vector1, vertor2):
    return np.dot(vector1, vertor2)

print(getDotProduct([1,2,3],[4,5,6,7,8]))