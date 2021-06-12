"""
4 Определить, какое число в массиве встречается чаще всего.
"""

import random
import timeit
import cProfile


SIZE = 10_000
MIN_ITEM = 0
MAX_ITEM = 25
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)


def method_3(array):
    cont = [0, '']
    for i in array:
        if cont[0] < array.count(i):
            cont[0], cont[1] = array.count(i), i

    return cont

# cont = method_3(array)
# print(f'Число {cont[1]} по вторяется {cont[0]} раз')

# сводные данные в фале report.txt

# 100
print(timeit.timeit('method_3(array)', number=100, globals=globals()))  # 0.009889645000000002
cProfile.run('method_3(array)')  # 28    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}

#500
# print(timeit.timeit('method_3(array)', number=100, globals=globals())) # 0.040463096000000004
# cProfile.run('method_3(array)')  # 30    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}

#1000
# print(timeit.timeit('method_3(array)', number=100, globals=globals()))  # 0.08095191499999999
# cProfile.run('method_3(array)')  # 29    0.001    0.000    0.001    0.000 {method 'count' of 'list' objects}

#10_000
# print(timeit.timeit('method_3(array)', number=100, globals=globals()))  # 0.58141548
# cProfile.run('method_3(array)')  # 28    0.004    0.000    0.004    0.000 {method 'count' of 'list' objects}

