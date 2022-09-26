import matplotlib.pyplot as plot
from sklearn.svm import LinearSVR
import numpy as np
import random


def some_func(x):
    return 2 * x + 17


def some_func_with_noise(x):
    noise = random.uniform(0, 1)
    return some_func(x) + noise


def get_args(num=100):
    return sorted([random.uniform(0, 10) for i in range(num)])


def svr(func, to_predict):
    lsvr = LinearSVR(verbose=0, dual=True)

    x_dataset = []
    y = []
    for x in get_args(num=80):
        x_dataset.append([x])
        y.append(func(x))

    lsvr.fit(np.array(x_dataset).reshape(-1, 1), y)
    print("Equation coef: ", lsvr.coef_)

    return lsvr.predict(np.array(to_predict).reshape(-1, 1))


src_args = get_args()
src_values = [some_func(x) for x in src_args]

args_for_noised_func = get_args()
noised_values = [some_func_with_noise(x) for x in args_for_noised_func]

plot.plot(src_args, src_values, label="src func")
plot.plot(args_for_noised_func, noised_values, label="noised func")
plot.plot(args_for_noised_func,
          svr(some_func, args_for_noised_func),
          label="predicted")

plot.legend()

plot.show()
