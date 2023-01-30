a = (1, 2, 'asd', ('as', 45, 3456, 'a'), 2, 2, 5.43)
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
print(id(a[3]))
print(id(a[4]))

print(len(a))
print('as' in a)
print('asd' in a)
print(('as', 45, 3456, 'a') in a)

b = ('r',)
print(b)
print(type(b))

c = tuple('r')
print(c)
print(type(c))

x1 = ('a', 't', 'v')
x2 = ('a', 't', 'v')

print(x1 == x2)
print(id(x1))
print(id(x2))
print(x1 is x2)

del a
print(a)
