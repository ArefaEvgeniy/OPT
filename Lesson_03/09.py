a = 1
b = 2.5
c = "2"

a1 = str(a)
c1 = int(c)

print(a + b)
print(type(a + b))

print(a + c1)
print(type(a + c1))

print(a1 + c)
print(type(a1 + c))

print(list((int(a1 + c) + a,)))
print(type(list((int(a1 + c) + a,))))
