# Написать функцию аргументом которой является целочисленный массив.
# Функция должна вернуть только уникальные значения для данного массива.

import math
import numpy as np

# Функция получения уникальных элементов массива/списка
def getUniqueElements(values):
    uniqueVal = set(values)
    if isinstance(values, list): return list(uniqueVal)
    elif isinstance(values, np.ndarray): return np.array(uniqueVal)
    elif isinstance(values, tuple): return tuple(uniqueVal)
    else: return uniqueVal

x = np.random.randint(1,4,20)
print(getUniqueElements(x))