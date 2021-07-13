"""
1. На улице встретились N друзей. Каждый пожал руку всем
остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""


s = int(input("Введите количество друзей: "))

graph = []
for i in range(s):
    line = [1] * s
    line[i] = 0
    graph.append(line)

print(*graph, sep='\n')

count = 0
for row in graph:
    for i in row:
        count += i

print(f"Ответ: {count}")
