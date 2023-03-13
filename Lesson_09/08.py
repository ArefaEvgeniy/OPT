def my_decorator(func):
    def wrapper():
        print('Я делаю что-то перед вызовом функции')
        func()
        print('Я делаю что-то после вызова функции')

    return wrapper


@my_decorator
def alone_function():
    print('I am alone function')


@my_decorator
def whisper(word='yes'):
    print(word.lower() + '...')


@my_decorator
def shout(word='Yes'):
    print(word.upper() + '!')


alone_function()
print('-' * 100)
whisper()
print('-' * 100)
shout()
# shout = my_decorator(shout)
