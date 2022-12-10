"""

2Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’]
и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в
несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование встроенных
функций для перевода из одной системы счисления в другую в данной задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

"""

import collections as call

print("Программа сложения и умножения шестнадцатиричных чисел")
a = list(input('Введи первое число: ').lower())
b = list(input('Введи второе число: ').lower())
action = input('Укажи действие ( + / * ): ')

a.reverse()
b.reverse()

hex_to_numbers_dic = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                      "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
numbers_to_hex_dic = {val: str(key) for key, val in hex_to_numbers_dic.items()}


def sum_hex(a, b, rev=False):
    if len(a) > len(b):
        b += ['0' for _ in range(len(a) - len(b))]
    elif len(b) > len(a):
        a += ['0' for _ in range(len(b) - len(a))]
    i = 0
    next_val = 0
    res = call.deque()
    while i < len(a):
        x = hex_to_numbers_dic.get(a[i]) + hex_to_numbers_dic.get(b[i])  # сложение текущего порядка
        res.appendleft(numbers_to_hex_dic[(next_val + x) % 16])
        next_val = x // 16  # перенос на следующий разряд
        i += 1

    if next_val > 0:  # добавляем в начало след разряд, если остался
        res.appendleft(numbers_to_hex_dic[next_val])

    if not rev:
        return "".join(res)
    else:
        res.reverse()
        return "".join(res)


def mult_hex(a, b):
    i = 0
    res = list()  # результат
    tmp1 = call.deque()
    tmp2 = call.deque()
    while i < len(a):
        k = 0
        next_val = 0
        tmp2.clear()
        while k < len(b):
            tmp1.clear()
            tmp1.extend('0' for _ in range(k))
            x = hex_to_numbers_dic.get(a[i]) * hex_to_numbers_dic.get(b[k])
            tmp1.append(numbers_to_hex_dic[(next_val + x) % 16])
            next_val = x // 16
            if next_val > 0:  # добавляем в начало след разряд, если остался
                tmp1.append(numbers_to_hex_dic[next_val])
            next_val = 0
            k += 1
            tmp2 = call.deque(sum_hex(tmp1, tmp2, True))

        tmp2.extendleft("0" for _ in range(i))
        res = list(sum_hex(tmp2, res, True))
        i += 1

    res.reverse()
    return "".join(res)


print("="*20)
if action == "+":
    print(sum_hex(a, b).upper())
elif action == "*":
    print(mult_hex(a, b).upper())
else:
    print("Действие введено неверно")
