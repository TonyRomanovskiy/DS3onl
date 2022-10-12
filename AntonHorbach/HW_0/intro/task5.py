from common.vectors import vec_len, rand_vec, vec_cos


def dot_product(f_vec, s_vec):
    return vec_len(f_vec) * vec_len(s_vec) * vec_cos(f_vec, s_vec)


for i in range(5):
    first_vec, second_vec = rand_vec(), rand_vec()
    product = dot_product(first_vec, second_vec)

    print(f"Dot product of {first_vec} and {second_vec} is {product}")


