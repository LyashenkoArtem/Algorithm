"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

n = input('Введите число: ')
chet = 0
nechet = 0

for i in range(len(n)):
    if int(n[i]) %2 == 0:
        chet += 1

    else:
        nechet += 1

print(f'В числе {n} - {chet} четных и {nechet} нечетных')