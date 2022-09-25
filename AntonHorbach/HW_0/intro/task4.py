import random
import math

from common.vectors import vec_len, rand_vec, vec_cos


def cosine_similarity(f_vec, s_vec):
    return vec_cos(f_vec, s_vec)


def cosine_distance(f_vec, s_vec):
    return 1.0 - cosine_similarity(f_vec, s_vec)


vectors = [rand_vec() for i in range(3)]

for first_vec in vectors:
    for second_vec in vectors:
        dist = cosine_distance(first_vec, second_vec)
        print(f"Cosine distance between {first_vec} and {second_vec} is {dist}")
