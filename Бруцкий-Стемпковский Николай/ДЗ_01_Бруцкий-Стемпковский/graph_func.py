import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.linear_model import LinearRegression

model = LinearRegression()

#создание исходного графика функции F = f(C)
F = lambda C: (C*1.8) + 32
C = np.linspace(-10, 20, 300)

#внесение случайной ошибки в функцию
C_rand = list(range(-10, 21))
F_rand = []
for i in C_rand:
    if random.randint(0, 9) < 6:
        F_rand.append(i*1.8 + 32)
    else:
        F_rand.append(i*1.8 + 32 + random.randint(-25, 25))

#создание массивов аргумента и функции на основе соответсвующего класса из NumPy
x = np.array(C_rand).reshape((-1, 1))
y = np.array(F_rand)

#линейная регрессия, оценка схожести исходного и испорченного массивов
model.fit(x, y)
r_sq = model.score(x, y)
b_0, b_1 = model.intercept_, model.coef_[0]

#построение "стабилизорованной" функции
C_stab = list(range(-10, 21))
F_stab = [i * b_1 + b_0 for i in C_stab]

#построение графика
fig = plt.subplot()
plt.plot(C, F(C))
plt.plot(C_rand, F_rand)
plt.plot(C_stab, F_stab)
plt.show()