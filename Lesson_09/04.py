# Создать собственную версию встроенной функции sum(). Функция sum()
# возвращает сумму всех элементов итерируемого объекта, переданных ей.

from functools import reduce

numerics = [1, 4, 66, 34, 224, 67, 34, 0, 99]


def custom_sum(a, b):
    return a + b


result = reduce(custom_sum, numerics)
print(result)

result_2 = reduce(lambda x, y: x + y, numerics)
print(result_2)
