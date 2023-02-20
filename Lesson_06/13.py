a = 'jjfru7663jkdkjf34459svbk2324009856jv'

b = [int(x) for x in a if '0' <= x <= '9']
print(b)


a = {1: 10, 2: 20, 3: 30}
b = [i * 2 for i in a]
print(b)
c = [i * a[i] for i in a]
print(c)


for item in a.items():
    print(item)
