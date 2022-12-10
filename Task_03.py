"""

3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в
другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то
используйте метод сортировки, который не рассматривался на уроках.

"""
import random as rnd

def counter(n, data):
    min_count, max_count, eq_count = 0, 0, 0
    for k in data:
        if k >= n:
            max_count += 1
        if k <= n:
            min_count += 1
        if k == n:
            eq_count += 1
    return min_count, max_count, eq_count

def get_mediana(data):
    for k in data:
        count = counter(k, data)

        if count[1] == count[0]:
            return k
        elif count[1] > count[0] and count[0] == count[1] - (count[2] - 1):
            return k
        elif count[1] < count[0] and count[1] == count[0] - (count[2] - 1):
            return k

    return None


# m = int(input("Ввведи целое число: "))
m = 2

array = [rnd.randint(0, 3) for _ in range(2*m+1)]
print(array)
print(get_mediana(array))
