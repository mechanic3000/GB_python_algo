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

def method_1(array):
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

        return cont

# print(f'Число {cont[1]} по вторяется {cont[0]} раз')

# сводные данные в фале report.txt

# 100
# print(timeit.timeit('method_1(array)', number=100, globals=globals()))  # 0.0012053140000000129
# cProfile.run('method_1(array)')  # 5    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}


#500
# print(timeit.timeit('method_1(array)', number=100, globals=globals())) # 0.005017479999999991
# cProfile.run('method_1(array)')  # 15    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}

#1000
# print(timeit.timeit('method_1(array)', number=100, globals=globals()))  # 0.010009788999999991
# cProfile.run('method_1(array)')  # 30    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}


#10_000
# print(timeit.timeit('method_1(array)', number=100, globals=globals()))  # 0.154322745
# cProfile.run('method_1(array)')  # 354    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}

