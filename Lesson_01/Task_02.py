"""
https://drive.google.com/file/d/1pIR6vCjN1aYUuXFeIz0jfwgHYGi9J7s-/view?usp=sharing

3.По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
"""

t = input("Введи любую строчную букву русского алфавита: ")

let_order = ord(t) - 1071
if let_order > 6:
    if let_order == 34:
        let_order = 7
    else:
        let_order += 1

print(f"Порядковый номер буквы \"{t}\" - {let_order}")