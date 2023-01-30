d = {1: 're', 2: 'aa', 'er': 2, 4: 're'}

print(d[2])
print(d.get(2, 'нет'))

print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

print(d[1])
print(id(d[1]))
print(d[4])
print(id(d[4]))

res = d.pop('er')
print(d)
print(res)

d.update({5: 55, 6: '66', 77: 'www'})
print(d)

f = {8: 88}

d.update(f)
print(d)
