'''
Определить, какое число в массиве встречается чаще всего.
'''
import random

a = [random.randint(1,10) for i in range(30)]
maximum = 0
n = 0
for i in range(len(a)):
    total = 0
    for j in range(len(a)):

        if a[i] == a[j]:
            total += 1
    if total > maximum:
        maximum, n = total, a[i]
print(a)
print(f'Число {n} встречается {maximum} раз')