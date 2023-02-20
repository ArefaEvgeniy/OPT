while True:
    input_string = input('Введите не более 3-х слов: ')
    if not input_string.strip():
        print('Пока')
        break
    else:
        if input_string.isdigit():
            input_string = int(input_string)
            if input_string == 0:
                print('Ноль')
            elif input_string % 2 == 0:
                print('Чётное')
            else:
                print('Не чётное')
        else:
            if input_string.lower() in ('да', 'нет'):
                print('ВВедено да или нет')
            else:
                if len(input_string.split()) > 3:
                    print('ВВедено бодее 3-х слов')
                else:
                    for item in input_string.split():
                        print(item)


while True:
    input_string = input('Введите не более 3-х слов: ')
    if not input_string.strip():
        print('Пока')
        break
    if input_string.isdigit():
        input_string = int(input_string)
        if input_string == 0:
            print('Ноль')
        elif input_string % 2 == 0:
            print('Чётное')
        else:
            print('Не чётное')
    elif input_string.lower() in ('да', 'нет'):
        print('Введено да или нет')
    elif len(input_string.split()) > 3:
        print('Введено более 3-х слов')
    else:
        for item in input_string.split():
            print(item)
