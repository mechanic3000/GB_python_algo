"""
https://drive.google.com/file/d/1N0id_BZzxTDzqaAkCGVv42jZJkU-ImdW/view?usp=sharing

7. Напишите программу, доказывающую или проверяющую,
 что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""


def make_summ(n, m=1):
    if n == m:
        return m
    else:
        return m+make_summ(n, m+1)


n = int(input("Введи количество натуральных чисел: "))
s = make_summ(n)
x = int(n*(n+1)/2)
print(f"Сумма чисел от 1 до {n} = {s}\nВыражение n(n+1)/2 = {x}\n{s}={x}")
if s == x:
    print("=> Равенство ВЕРНО.")
else:
    print("=> Равенство НЕВЕРНО")
