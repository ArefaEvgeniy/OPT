import copy

a = [1, 2, ['a', 'b', 'c'], 3, 4]
b = copy.deepcopy(a)
c = a[:]
d = a.copy()

b.insert(0, 0)
c.append(5)
d.insert(2, 2)
b[3].append('d')

print(a)
print(b)
print(c)
print(d)
