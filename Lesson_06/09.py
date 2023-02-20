value_1 = int(input('Введите первое число: '))
value_2 = int(input('Введите второе число: '))

if value_1 > value_2:
    value_1, value_2 = value_2, value_1

for item in range(value_1, value_2 + 1):
    if item == value_2:
        print(item)
    else:
        print(item, end=', ')

print('N =', value_2 - value_1 + 1)
