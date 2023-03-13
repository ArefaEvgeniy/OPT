def shout(word='Yes'):
    print(word + '!')


def do_some_before(func):
    print('Я делаю что-то перед вызовом функции')
    func()


def do_some_before_after(func):
    print('Я делаю что-то перед вызовом функции')
    func()
    print('Я делаю что-то после вызова функции')


do_some_before_after(shout)
