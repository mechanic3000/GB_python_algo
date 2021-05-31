"""
https://drive.google.com/file/d/1WkpQsRe_qdLap6umR3NDd4ZSn9t_toO_/view?usp=sharing

8.Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

print("Введи три разных числа")
a = int(input("Введи первое число: "))
b = int(input("Введи второе число: "))
c = int(input("Введи третье число: "))

if a > b and a > c:
    if c > b:
        m = c
    else:
        m = b
else:
    if c > b and c > a:
        if a > b:
            m = a
        else:
            m = b
    else:
        if c > a:
            m = c
        else:
            m = a

print(f"Среднее по виличине число - {m}")
