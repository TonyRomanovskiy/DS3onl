# Напишите функцию, которая принимает на вход два вектора и возвращает косинусное расстояние данных векторов.

import math
import numpy as np

# Функция расчета косинусного расстояния векторов
def getСosineSimilarity(vector1, vector2):
    return np.dot(vector1, vector2) / (np.linalg.norm(vector1)*np.linalg.norm(vector2))

print(getСosineSimilarity([1,2,3],[1,2,3]))