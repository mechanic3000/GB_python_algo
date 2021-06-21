import random
from collections import Counter
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


most_common = Counter(array).most_common()[0]

do_sum_of_used_mem(array)
do_sum_of_used_mem(most_common)
print(USED_MEM)
print(f'Число {most_common[0]} по вторяется {most_common[1]} раз')
