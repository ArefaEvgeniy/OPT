# Создать lambda функцию, которая принимает на вход список имен
# и выводит их в формате “Hello, {name}” в другой список.
# Все имена должны быть написаны строчными буквами и с заглавной первой

name_list = ['Bob', 'jack', 'NENCI', 'EriC']
new_list = lambda x: [f'Hello, {name.title()}' for name in x]
print(new_list(name_list))
