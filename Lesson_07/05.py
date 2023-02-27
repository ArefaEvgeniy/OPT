def aaa(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)
    return 33


aaa(55, None, {3, 4, 5}, d=[1, 2, 3], a=0)
