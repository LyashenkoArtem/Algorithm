import random
import timeit
import cProfile
import sys

# №1 создание матрицы двумя циклами
def m_create_2_for(range_raw, range_coll):
    matrix = [[random.randint(1, 100) for _ in range(1, range_coll)] for _ in range(1, range_raw)]


#--------------------------------------------------------------------------------------------------


# №2 Создание матрицы 1 циклом
def m_create_1_for(size_matrix):
    matrix = []
    temp_array = []

    for i in range(1, (size_matrix ** 2) + 1):
        val = random.randint(1, 100)

        if i % size_matrix == 0:
            temp_array.append(val)
            matrix.append(temp_array)
            temp_array = []
        else:
            temp_array.append(val)
    print(matrix)


# --------------------------------------------------------------------------------------------------


# №3 Создание матрицы рекурсией
sys.setrecursionlimit(2000)

def m_create_recursion(range_raw, range_coll, coll_count=0, f_matrix = []):
    matrix = []
    if coll_count + 1 == range_coll:
        for _ in range(range_raw):
            matrix.append(random.randint(1, 100))
        f_matrix.append(matrix)
        return f_matrix
    else:
        for _ in range(range_raw):
            matrix.append(random.randint(1, 100))
        coll_count += 1
        f_matrix = m_create_recursion(range_raw, range_coll, coll_count)
        f_matrix.append(matrix)
        return f_matrix