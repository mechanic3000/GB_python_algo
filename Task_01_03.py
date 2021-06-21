import random
from sys import getsizeof


SIZE = 1_000
MIN_ITEM = 0
MAX_ITEM = 25
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

USED_MEM = 0


def do_sum_of_used_mem(a):
    global USED_MEM
    USED_MEM += getsizeof(a)
    return None


cont = [0, '']
for i in array:
    if cont[0] < array.count(i):
        cont[0], cont[1] = array.count(i), i

do_sum_of_used_mem(array)
do_sum_of_used_mem(cont)
do_sum_of_used_mem(i)
print(USED_MEM)
print(f'Число {cont[1]} по вторяется {cont[0]} раз')
