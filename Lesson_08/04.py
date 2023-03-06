# Написать программу для поиска в списке определённого слова
# При этом список может состоять из разного типа данных
# и иметь не ограниченное число вложенных друг в друга списков или кортежей
# поиск произвести по всем списка и кортежам, в том числе и вложенным

INPUT_LIST = [
    1,
    '2',
    'cat',
    99,
    'dog',
    (4, 44, ['red', 'green', ('mother', 'father', ['a', 'd', ['z', 'ww']])]),
    ['one', 'two', '55', {1, 4, 'big', True}, ['milk', 0, 'bred']],
    'End'
]


def find_world(world, input_list):
    result = False
    for item in input_list:
        if isinstance(item, (str, int)) and str(item) == world:
            result = True
            break
        elif isinstance(item, (tuple, list, set)):
            result = find_world(world, item)
            if result:
                break
    return result


res = find_world(input('Введите слово для поиска: '), INPUT_LIST)
print('Слово найдено' if res else 'Слово не найдено')
