#Карпеченко Д.М., dz07, v.0.1, 01.10.2022

import random
#создаем лист со случайной переменной
a = [random.randint(1,10)]

#создаем декоратор
def count_calls(func):

    def wrapper_count_calls(*args, **kwargs):
# Проверяем, если наш счетчик вызова функции кратен 3, то сбрасываем наши значения листа
# и выполняем функцию дальше
        if wrapper_count_calls.num_calls%3==0:
            global a
            a=[random.randint(1,10)]
            wrapper_count_calls.num_calls += 1
            print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
            print(a)
            return func(*args, **kwargs)
# Если счетчик вызова не кратен трем, то увеличиваем на один и выводим результат
        else:
            wrapper_count_calls.num_calls += 1
            print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
            print(a)
            return func(*args, **kwargs)

    wrapper_count_calls.num_calls = 0
    wrapper_count_calls.counter = 0

    return wrapper_count_calls

#наша декорируемая функция которая просто генерирует случайные числа
@count_calls
def a1():
    return a.append(random.randint(1,10))
