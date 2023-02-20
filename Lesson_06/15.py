old_dict = {'aa': 1, 'b': 2, 'cccc': 3}

new_dict = {key + str(len(key)): value ** 2 for key, value in old_dict.items() if value % 2 != 0}

print(new_dict)
