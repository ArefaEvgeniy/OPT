value = "Меня зовут %(name)s. Мне %(age)s лет. Мне нравится имя %(name)s"

value_1 = "Меня зовут "
value_2 = ". Мне "
value_3 = " лет. Мне нравится имя "

name = 'Jack'
age = 43

print(value % {"name": name, "age": age})
