a = 'text'
b = 'text 2'
c = 'text'

print(id(a))
print(id(b))
print(id(c))
print(a == c)
print(a is c)

d = a + ' 2'
# d = 'text 2'
print(a)
print(id(a))
print(a + ' 2' == b)
print(a + ' 2' is b)

print(d)
print(id(d))
print(d == b)
print(d is b)


e = 246
f = 246
y = 400

print(id(e))
print(id(f))
print(id(y))
print(e == f)
print(e is f)
