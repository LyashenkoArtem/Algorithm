'''
Написать программу, которая генерирует в указанных пользователем границах:

a. случайное целое число,

b. случайное вещественное число,

c. случайный символ.
'''

import random

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if a < b:
    pass

elif a > b:
    a, b = b, a

else:
    print('Вы ввели одинаковые числа')


num1 = random.randint(a, b)
num2 = random.uniform(a, b)

let_1 = input('Введите букву: ')
let_2 = input('Введите вторую букву: ')

let_1 = ord(let_1)
let_2 = ord(let_2)

num3 = random.randint(let_1, let_2)

let = chr(num3)

print(num1, num2, let)