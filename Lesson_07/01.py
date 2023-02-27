def add(a, b):
    def sub(a, b):
        a -= 1
        b -= 1
        print('a local:', a)
        print('b local:', b)
        return 33

    a += 1
    b += 2
    print('a:', a)
    print('b:', b)
    sub(a, b)
    return a + b


a = 10  # 0000914
b = 5   # 1000914
print(add(a, b))
print('a global:', a)
print('b global:', b)
