'''
В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''

import random

a = [random.randint(1,20) for i in range(20)]
maximum = 0
minimum = 100
total = 0
n = 0
m = 0

for i in range(len(a)):
    if a[i] >= maximum:
        maximum = a[i]
        m = i

    if a[i] <= minimum:
        minimum = a[i]
        n = i
if n > m:
    n,m = m,n

for i in range(n+1, m):
    total += a[i]

print(a)
print(f'Максимальное число : {maximum}, а минимальное: {minimum}')
print(total)