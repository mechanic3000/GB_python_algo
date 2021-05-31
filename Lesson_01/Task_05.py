"""
https://drive.google.com/file/d/1T3evDioIsGRfoh7PKoqOJ2ckr9y3N1te/view?usp=sharing

5.Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

n = int(input("Введи поряднковый номер буквы латинского алфавита: "))+96

letter = chr(n)

print(f"Вы ввели номер буквы '{letter}'")
