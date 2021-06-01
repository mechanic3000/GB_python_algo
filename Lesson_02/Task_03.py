"""
https://drive.google.com/file/d/1wYz7n2CbSpp_Bg99fZMHkc11FS4kKG2T/view?usp=sharing

3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


def rev_digit(n, r=''):
    a = n % 10
    r += str(a)

    if n//10 == 0:
        return r
    else:
        return rev_digit(n//10, r)


n = int(input("Введи число: "))

z = rev_digit(n)

print(f'Обратное число - {z}')
