my_pets = ['alfred', 'tabitha', 'william', 'arla']


upper_pets = []
for pet in my_pets:
    upper_pets.append(pet.upper())
print(upper_pets)


upper_pets_2 = list(map(str.upper, my_pets))
print(upper_pets_2)


def my_upper(x):
    return x.upper()


upper_pets_3 = list(map(my_upper, my_pets))
print(upper_pets_3)

upper_pets_4 = list(map(lambda x: x.upper(), my_pets))
print(upper_pets_4)
