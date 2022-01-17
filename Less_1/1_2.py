'''
По введенным пользователем координатам двух точек вывести
уравнение прямой вида y = kx + b, проходящей через эти точки.
'''

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

print('Найдем выражение у = kx + b')

k = (y_2 - y_1)/ (x_2 - x_1)
b = y_1 - (y_2 - y_1)/ (x_2 - x_1) * x_1

print(f'k = {k},b = {b}')
print(f'Выражение имеет вид: y = {k}x + {b}')