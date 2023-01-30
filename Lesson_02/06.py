a = "It's a simple, text"

print(a[1:-1])
print(a[1:])

print(a[16])
print(a[-2])

print(a[0:-2])
print(a[:-2])

b = a[::-1]
print(b)
print(a.title())
print(a)

print(a.find('e'))
print(a.rfind('e'))

print(a.rfind('simple '))

print('quit' in a)
