lst = ['a', 'f', 2, 6, 't', 'rr', 'tr']

target = 2

for index, item in enumerate(lst):
    if item == target:
        break
else:
    index = -1

print('Index:', index)
