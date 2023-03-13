def shout(word='Yes'):
    return word + '!'


print(shout())

screem = shout
print(screem())

del shout
print(screem())
