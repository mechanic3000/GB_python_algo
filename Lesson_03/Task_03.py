"""
3 В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


for i, item in enumerate(array):
    try:
        if item < min_items[1]:
            min_items[0], min_items[1] = i, item
    except NameError:
        min_items = [i, item]

    try:
        if item > max_items[1]:
            max_items[0], max_items[1] = i, item
    except NameError:
        max_items = [i, item]

array[min_items[0]], array[max_items[0]] = max_items[1], min_items[1]
print(array)
