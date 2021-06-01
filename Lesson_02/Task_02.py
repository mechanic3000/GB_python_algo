"""
https://drive.google.com/file/d/1DhVNHfPDSl79CJ7BVxH4Q94TMATzMmms/view?usp=sharing

2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def count_digit(n, x=0, y=0):
    a = n % 10
    if a % 2 == 0:
        x += 1
    else:
        y += 1

    if n // 10 == 0:
        return f'Количество четных чесиел - {x}\nКоличество нечетных чисел - {y}'
    else:
        return count_digit(n // 10, x, y)


n = int(input('Введи натуральное число: '))
z = count_digit(n)
print(z)
