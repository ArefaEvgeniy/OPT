a = 7

if a >= 0:
    b = True
else:
    b = False

b = 5 if a >= 10 else 6 if a >= 0 else False
print(b)


nice = False
personality = ("good", "bad")[nice]
print("Cat is", personality)
