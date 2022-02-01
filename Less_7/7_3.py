'''
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда,
делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки,
который не рассматривался на уроках (сортировка слиянием также недопустима).
'''
import random

m = int(input('Длинна массива 2м + 1. Введите число м: '))
arr = [random.randint(1, 100) for i in range(2*m +1)]
a = []
b = []
print(f'Исходный массив: {arr}')
media = (max(arr) + min(arr)) // 2

while media not in arr:
    media += 1


for el in arr:
    if el < media:
        a.append(el)

    else:
        b.append(el)


b.remove(media)

while len(a) != len(b):
    if len(a) < len(b):

        a.append(media)

        media = b.pop(b.index(min(b)))


    elif len(a) > len(b):

        b.append(media)
        media = a.pop(a.index(max(a)))

print(f'Медиана: {media}')
print(f'Числа меньше медианы: {a}')
print(f'Числа больше медианы: {b}')
