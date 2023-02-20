a = None

if a is True:
    b = 1
else:
    if a is None:
        b = -1
    else:
        b = 0
print(b)


b = 1 if a is True else -1 if a is None else 0
print(b)
