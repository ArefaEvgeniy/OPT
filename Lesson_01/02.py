from langdetect import detect

a = "This is English"
b = "Это русский язык"
c = "Це українська мова"

lang_a = detect(a)
print(lang_a)
print(detect(b))
print(detect(c))
