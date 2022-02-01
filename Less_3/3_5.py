'''
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''
import random

a = [random.randint(-100, 100) for i in range(100)]
maximum = -100

for i in range(len(a)):
    if a[i] < 0:
        if a[i] > maximum:
            maximum = a[i]

print(a)
print(maximum)