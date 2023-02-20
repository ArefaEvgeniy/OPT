lst = ['a', 'f', 2, 6, 't', 'rr', 'tr']

target = 'zz'

index = 0
while index < len(lst):
    if lst[index] == target:
        break
    index += 1
else:
    index = -1

print('Index:', index)
