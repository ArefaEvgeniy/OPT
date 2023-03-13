a = [1, 2, 3, 4]


def func(d):
    print(f'd before: {d}')
    d.append(9)
    print(f'd after: {d}')


print(f'a before: {a}')
func(a[0:])
print(f'a after: {a}')
print('-' * 100)


def func_2(d=None):
    if d is None:
        d = [1, 2, 3]
    d.append(len(d))
    return d


print(func_2([5, 6, 7, 8]))
print(func_2([1, 2]))
print(func_2())
print(func_2([]))
print(func_2())
print(func_2())
print(func_2([0]))
print(func_2())
print(func_2([1, 2, 3]))
print(func_2())
