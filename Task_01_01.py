"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

4 Определить, какое число в массиве встречается чаще всего.
"""

import random
from sys import getsizeof

USED_MEM = 0


def do_sum_of_used_mem(a):
    global USED_MEM
    USED_MEM += getsizeof(a)
    return None


SIZE = 1_000
MIN_ITEM = 0
MAX_ITEM = 25
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


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

do_sum_of_used_mem(array)
do_sum_of_used_mem(array)
do_sum_of_used_mem(cont)
do_sum_of_used_mem(k)
do_sum_of_used_mem(b)
do_sum_of_used_mem(s)
do_sum_of_used_mem(i)

print(USED_MEM)
print(f'Число {cont[1]} по вторяется {cont[0]} раз')
