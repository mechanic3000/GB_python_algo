"""
https://drive.google.com/file/d/15yosa5gl_aqK5eaS_HFSmQfiTBIyBz93/view?usp=sharing

2.По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей
через эти точки.
"""

x1 = float(input("Введи X первой точки: "))
y1 = float(input("Введи Y первой точки: "))
x2 = float(input("Введи X второй точки: "))
y2 = float(input("Введи Y второй точки: "))

a = y1 - y2
b = x2 - x1
c = x1*y2 - x2*y1

print(f'у={a/b}x {"+" if c/b > 0 else ""}{c/b}')
