"""
4 Определить, какое число в массиве встречается чаще всего.
"""

import random
from collections import Counter
import timeit
import cProfile

SIZE = 10_000
MIN_ITEM = 0
MAX_ITEM = 25
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def method_2(array):
    array_counter = Counter(array)

    return array_counter.most_common()[0]

# cont = method_2(array)
# print(f'Число {cont[0]} по вторяется {cont[1]} раз')

# сводные данные в фале report.txt

# 100
print(timeit.timeit('method_2(array)', number=100, globals=globals()))  # 0.002490868999999993
cProfile.run('method_2(array)')


#500
# print(timeit.timeit('method_2(array)', number=100, globals=globals())) #  0.00846544299999999
# cProfile.run('method_2(array)')

#1000
# print(timeit.timeit('method_2(array)', number=100, globals=globals()))  # 0.014040051999999997
# cProfile.run('method_2(array)')


#10_000
# print(timeit.timeit('method_2(array)', number=100, globals=globals()))  # 0.08897391700000001
# cProfile.run('method_2(array)')

