import random


def get_not_unique_arr(size=10):
    rand_arr = [random.uniform(0, 100) for i in range(size)]
    shuffled_arr = rand_arr.copy()
    random.shuffle(rand_arr)

    for i in range(len(rand_arr)):
        if random.randint(0, 1) != 0:
            rand_arr[i] = shuffled_arr[i]

    return rand_arr


def get_unique(arr):
    # return set(arr)
    result = []

    for val in arr:
        if val not in result:
            result.append(val)

    return result


src_arr = get_not_unique_arr()
print("Src: ", src_arr)

print("Result: ", get_unique(src_arr))
