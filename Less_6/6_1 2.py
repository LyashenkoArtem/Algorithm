import random
import sys
a = random.randint(1, 10)
# №1 создание матрицы двумя циклами
matrix = [[a for _ in range(1, 10)] for _ in range(1, a)]
print(matrix)
print(sys.getsizeof(matrix))
print('*'*50)

# №2 Создание матрицы 1 циклом
matrix = []
temp_array = []
size_matrix = a

for i in range(1, (size_matrix ** 2)):
    val = a

    if i % size_matrix == 0:
        temp_array.append(val)
        matrix.append(temp_array)
        temp_array = []
    else:
        temp_array.append(val)
print(matrix)
print(sys.getsizeof(matrix))
print('*'*50)

# №3 Создание матрицы рекурсией
sys.setrecursionlimit(2000)

def m_create_recursion(range_raw, range_coll, coll_count=0, f_matrix = []):
    matrix = []
    if coll_count + 1 == range_coll:
        for _ in range(range_raw):
            matrix.append(random.randint(1, 10))
        f_matrix.append(matrix)
        return f_matrix
    else:
        for _ in range(range_raw):
            matrix.append(random.randint(1, 10))
        coll_count += 1
        f_matrix = m_create_recursion(range_raw, range_coll, coll_count)
        f_matrix.append(matrix)
        return f_matrix
print(m_create_recursion(a, a))
print(sys.getsizeof(m_create_recursion))



''' 
x86_32 MacOs 10.14.6 (18G103)
Python 3.10

При создании матриц, объем занимаемой памяти примерно соизмерим
первый способ:
создание матрицы 6х6 занимает 120 бит памяти
второй способ 
создание матрицы 6х6 занимает 120 бит памяти
третий способо 
создание матрицы 6х6 занимает 144 бит памяти
'''