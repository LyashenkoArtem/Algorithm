'''
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''
from collections import  namedtuple

n = int(input('Введите колпичество предприятий: '))
base = {}
total = 0
media = 0

Pred = namedtuple('Pred', 'name, q1, q2, q3, q4, total_ent')

for i in range(n):
    name_ent = input(f'Введите название {i+1}-ого предприятия: ')
    q1_ent = int(input('Прибыль за 1 квартал: '))
    q2_ent = int(input('Прибыль за 2 квартал: '))
    q3_ent = int(input('Прибыль за 3 квартал: '))
    q4_ent = int(input('Прибыль за 4 квартал: '))

    total_ent = q1_ent + q2_ent + q3_ent + q4_ent
    total += q1_ent + q2_ent + q3_ent + q4_ent

    base[name_ent] = Pred(name_ent,q1_ent, q2_ent, q3_ent, q4_ent, total_ent)

media = total / n
print(f'Средний доход всех {n} предприятий - {media}')
print('Предприятия, доход которых больше среднего: ')

for name_ent, total_ent in base.items():
    if base[name_ent].total_ent > media:
        print(f'Прибыль предприятия {name_ent} - {base[name_ent].total_ent}')
