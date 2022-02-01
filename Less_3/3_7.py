'''
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
'''

import random

a = [random.randint(1,100) for i in range(20)]
print(a)

n = min(a)
a.remove(n)

m = min(a)

print(n, m)