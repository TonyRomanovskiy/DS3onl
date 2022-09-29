import math
import numpy
import scipy

def unic_value(array):
    #эта функция находит уникальные значения в списке array
    return [x for x in range(len(array)) if array.count(x) == 1]

array = [1, 2, 2, 3, 4, 5, 6, 6]
#print(unic_value(array))

arr1 = [1, 1, 2]
arr2 = [1, 1, 1]

def scalar_product(arr1, arr2):
    #эта функция находит скалярное произведение двух векторов arr1 и arr2
    if len(arr1) == len(arr2):
        len_ = len(arr1)
        return sum([arr1[i]*arr2[i] for i in range(len_)])

#print(scalar_product(arr1, arr2))

def scalar_product_numpy(arr1, arr2):
    #эта функция делает то же самое, но используя средства из модуля NumPy
    return numpy.dot(arr1, arr2)

#print(scalar_product_numpy(arr1, arr2))

def cos_distance(arr1, arr2):
    #эта функция определяет косинусное расстояние двух векторов
    #numerator - числитель (в нем скалярное произведение этих векторов)
    #denominator - знаменатель (в нем сумма корней суммы квадратов элементов векторов)
    len_ = len(arr1)
    numerator = scalar_product(arr1, arr2)
    denominator = (math.sqrt(sum([arr1[i]**2 for i in range(len_)])) *
                    math.sqrt(sum([arr2[i]**2 for i in range(len_)])))
    #return numerator/denominator #вернуть подобие вместо разности
    return 1 - numerator/denominator

#print(cos_distance(arr1, arr2))

def cos_distance_scipy(arr1, arr2):
    #эта функция делает то же самое, но используя средства из модуля SciPy
    return scipy.spatial.distance.cosine(arr1, arr2)

#print(cos_distance_scipy(arr1, arr2))