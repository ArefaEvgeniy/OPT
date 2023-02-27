def aaa():
    print('aaa')
    return 12, 45, 'FFF'


a, b, c = aaa()
print(a)
print(b)
print(c)
print('-' * 50)


def bbb(a, f, g=99, h=0):
    print('a:', a)
    print('f:', f)
    print('g:', g)
    print('h:', h)


bbb(55, 0.0, 1)
print('-' * 50)


def ccc(a, f, g, h=-3):
    print('a:', a)
    print('f:', f)
    print('g:', g)
    print('h:', h)


ccc(g=33, f=22, h=55, a=99)
print('-' * 50)
