"""
Запросить у пользователя два целых числа.
Вывести строку вида “2 плюс 3 равно 5”
"""


import datetime


num = input("Введите два числа через пробел: ")
num = num.split()
num_1 = int(num[0])
num_2 = int(num[1])

now = datetime.datetime.now()
print("%d плюс %d равно %d" % (num_1, num_2, num_1 + num_2))
print('Time spend:', datetime.datetime.now() - now)

now = datetime.datetime.now()
print("{} плюс {} равно {}".format(num_1, num_2, num_1 + num_2))
print('Time spend:', datetime.datetime.now() - now)

now = datetime.datetime.now()
print(f"{num_1} плюс {num_2} равно {num_1 + num_2}")
print('Time spend:', datetime.datetime.now() - now)


sales_tax_10 = 1.10
