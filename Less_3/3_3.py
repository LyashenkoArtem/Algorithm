'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

import random

a = [random.randint(0, 100) for i in range(random.randint(10,20))]
maximum = 0
minimum = 100
n, m = 0, 0

print('Исходный массив')
print(a)

for i in range(len(a)):

    if a[i]> maximum:
        maximum = a[i]
        n = i

    if a[i] < minimum:
        minimum = a[i]
        m = i

print()
print(f'Максимум равен  {maximum} и находится на {n} месте. Минимум {minimum} на {m} месте')

a[n], a[m] = minimum, maximum

print()
print('Меняем местами значения: ')
print(a)