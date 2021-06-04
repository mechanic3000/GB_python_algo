"""
6 В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 200
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


for i, item in enumerate(array):
    try:
        if item < min_item[1]:
            min_item[0], min_item[1] = i, item
    except NameError:
        min_item = [i, item]

    try:
        if item > max_item[1]:
            max_item[0], max_item[1] = i, item
    except NameError:
        max_item = [i, item]

print(min_item, max_item, '[поз, число]', sep=' - ')

if max_item[0] > min_item[0]:
    k = 1
else:
    k = -1

i = min_item[0]
s = 0

while i != max_item[0]+k*-1:
    s += array[i+k]
    i += k

print(f'Сумма элементов массива между МАКС и МИН числами = {s}')