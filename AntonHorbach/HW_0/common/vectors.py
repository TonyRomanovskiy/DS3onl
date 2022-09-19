import random
import math


def rand_vec(dim=3):
    return [random.uniform(-100, 100) for i in range(dim)]


def vec_len(vec):
    return math.sqrt(sum(i**2 for i in vec))


def vec_cos(f_vec, s_vec):
    return sum(f * s for f, s in zip(f_vec, s_vec)) / (vec_len(f_vec) * vec_len(s_vec))
