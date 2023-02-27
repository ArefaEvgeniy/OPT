def aaa(*args):
    print('args:', args)
    print('type:', type(args))
    res = 0
    for item in args:
        res += item
    return res


res = aaa(1, 2, 3, 4, 5, 6, 7, 5, 99)
print('res:', res)
