'''
Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого).
'''

a = int(input('Введите первое из трех целое число: '))
b = int(input('Введите второе из трех целое число: '))
c = int(input('Введите третье число: '))

max_num = max(a,b,c)
min_num = min(a,b,c)
sred_num = a + b + c - min_num - max_num

print('Среднее число: ', sred_num)

'''
РЕШЕНИЕ ЧЕРЕЗ ЦИКЛ
'''

if a > b:
    if b > c:
        centr = b

    else:
        if a > c:
            centr = c
        else:
            centr = a

else:
    if a > c:
        centr = a

    else:
        if b > c:
            centr = c
        else:
            centr = b


print(centr)