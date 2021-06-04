"""
4 Определить, какое число в массиве встречается чаще всего.

"""

import datetime
import random

SIZE = 300
MIN_ITEM = 0
MAX_ITEM = 25
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
array_c = array.copy()
cont = [0] * 2

for i in set(array):
    k = 0
    b = True
    s = 0  # позиция элемента, чтоб продолжить с того же места

    while b:
        try:
            s = array_c.index(i, s)
            array_c.pop(s)

            k += 1
        except ValueError:
            b = False

    if cont[0] < k:
        cont[0], cont[1] = k, i

print(f'Число {cont[1]} по вторяется {cont[0]} раз')
