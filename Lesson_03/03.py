a = [1, 2, 'asd', 2, 2, 5.43]
f = list((1, 2, 3, 4))

print(id(a))
print(len(a))

a.append('p')
print(a)
print(id(a))

a.insert(0, 'a')
print(a)
print(id(a))

a.insert(3, ['d', 'g', [('a', 'b', ''), 1, 2, 3], 'h'])
print(a)
print(id(a))

res1 = a.remove(2)
print(a)
print(id(a))

a[1] = 0
print(a)

del a[3]
print(a)

b = [1, 2, 3, 4, 5]
c = [6, 7, 8, 9]

b.extend(c)
print(b)

b += c
print(b)

print(a)
print(a[2][2][0][1])

print(a)
res2 = a.pop()
print(a)

print(res1)
print(res2)

print(f)
