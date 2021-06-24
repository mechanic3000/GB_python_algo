"""

2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

"""
import random as rnd


def merge_sort(data):
    len_data = len(data)
    if len_data < 2:
        return data
    else:
        left_part = merge_sort(data[:len_data//2])  # разбиваем список пополам, пока не ост. 1 эл в списке
        right_part = merge_sort(data[len_data//2:])

        i, j = 0, 0
        result = []
        len_left, len_right = len(left_part), len(right_part)
        while i < len_left or j < len_right:
            if i >= len_left:
                result.append(right_part[j])
                j += 1
            elif j >= len_right:
                result.append(left_part[i])
                i += 1
            elif left_part[i] > right_part[j]:
                result.append(right_part[j])
                j += 1
            else:
                result.append((left_part[i]))
                i += 1

        return result


array = [rnd.randint(0, 49) for _ in range(11)]
print(array)
array = merge_sort(array)
print(array)
