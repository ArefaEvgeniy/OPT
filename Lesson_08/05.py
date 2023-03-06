def hello(name: (str, list, tuple) = 'NoName', age: int = 0) -> str:
    """Функция приветствует пользователя"""
    new_age = age + 1
    print(f'Hello, {name}')
    return f'Hello, {name}'


print(hello.__annotations__)
print(hello.__doc__)
hello()
