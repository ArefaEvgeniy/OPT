from datetime import datetime

n = int(input('Введите любое натуральное число: '))


def factorial_1(n):
    q = 0
    result = 1
    while n > q:
        q += 1
        result *= q
    return result


def factorial_2(n):  # n = 5
    if n == 0:
        return 1
    else:
        return n * factorial_2(n - 1)  # 120


now = datetime.now()
print(factorial_1(n))
print('time: ', datetime.now() - now)
print('-' * 100)
now = datetime.now()
print(factorial_2(n))
print('time: ', datetime.now() - now)
