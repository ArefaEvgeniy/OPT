def aaa(a, step=None):
    if step is None:
        step = []
    for item in range(a):
        step.append(item)
    return step


res = aaa(5, [99, 100])
print(res)

res = aaa(3, [99, 1])
print(res)

res = aaa(10)
print(res)

res = aaa(4)
print(res)

res = aaa(8)
print(res)

res = aaa(3, [99, 1])
print(res)

res = aaa(2)
print(res)
