def aaa(d, e, **kwargs):
    print('d:', d)
    print('e:', e)
    print('kwargs:', kwargs)
    print('type:', type(kwargs))


aaa(22, 33, a=3, b=4, c=0)
