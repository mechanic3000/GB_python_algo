"""

1. Определить количество различных подстрок с использованием хеш-функции. Задача: на вход функции дана строка,
требуется вернуть количество различных подстрок в этой строке.

Примечание: в сумму не включаем пустую строку и строку целиком.

"""
import hashlib as hl


def substr_counter(string):
    k = 1  # количество символов в подстроке
    trash = set()
    len_string = len(string)
    while k < len_string:
        for i in range(0, len_string + 1):
            # trash.add(string[i:i + k])
            trash.add(hl.sha1(string[i:i + k].encode('utf-8')).hexdigest())
            # trash.add(hash(string[i:i + k]))
        k += 1

    return len(trash) - 1


c = "Примечание: в сумму не включаем пустую строку и строку целиком."
print(substr_counter(c))
