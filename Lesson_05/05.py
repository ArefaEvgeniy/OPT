japan_str = 'ぁぃえおき げず㍿ボ゛'
japan_char = '㍿'

color = 'red'
name = 'Tom'
surname = 'Арефа'

print(japan_str.encode())
print(japan_char.encode())
print(color.encode())
print(name.encode())
print(surname.encode())

aa = surname.encode()

print('aa:', aa)
print('aa:', aa.decode(encoding='Latin1'))
