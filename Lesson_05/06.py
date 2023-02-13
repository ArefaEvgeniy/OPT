# Дана переменная artist_bytes в байтовом виде.
# Декодировать её в юникод и вывести на экран.
# Декодирование значение закодировать в кодировке 'Latin1'


artist_bytes = b'Tage \xc3\x85s\xc3\xa9n'

print(type(artist_bytes))
print(len(artist_bytes))

artist_utf_8 = artist_bytes.decode()
print(artist_utf_8)
print(type(artist_utf_8))

artist_utf_32 = artist_utf_8.encode(encoding='utf-32')
print(artist_utf_32)
print(len(artist_utf_32))

artist_latin_1 = artist_utf_8.encode(encoding='Latin1')
print(artist_latin_1)
print(type(artist_latin_1))
print(len(artist_latin_1))

print(artist_latin_1.decode(encoding='Latin1'))

