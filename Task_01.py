"""

1 Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
 Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
 предприятий,
чья прибыль выше среднего и ниже среднего.

"""

import collections as coll

firms = coll.Counter()
Q_COUNT = 4  # количество периодов для расчета

for i in range(int(input("Введи количество предприятий: "))):
    print(f'\nВвод данных по фирме номер {i+1}')
    firm_name = input(f'Введи название фирмы № {i+1}: ')
    for q in range(Q_COUNT):
        firms[firm_name] += int(input(f'Введи выручку за {q+1}-й квартал: '))
    firms[firm_name] = firms[firm_name]/Q_COUNT

avg_firms = sum(firms.values())/len(firms)
print(f'\nСредний годовой доход по всем фирмам = {avg_firms}')
firms['--------------'] = avg_firms

print("="*20+'\n')
for firm, value in firms.most_common():
    print(firm, value, sep=" - ")

