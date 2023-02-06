value = "Меня зовут {name}. Мне {age} лет. Мне нравится имя {name}"

value_1 = "Меня зовут "
value_2 = ". Мне "
value_3 = " лет. Мне нравится имя "

name = 'Jack'
age = 43

print(value.format(age=age, name=name))

print('start {:_^30} end'.format(name))

a = round(3.13159, 3)
b = 0.7512

print('{}'.format(a))
print('{:.2%}'.format(b))

print('{:x}'.format(123))
