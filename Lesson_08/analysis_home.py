from random import randint


def user():
    while True:
        number_user = input('Введіть ваше число від 1 до 10: ', )
        if number_user.isdigit():
            number_user = int(number_user)
            break
    return number_user


def work(number_user):
    allempt = 1
    while allempt <= 3:
        if number_random == number_user:
            print('Молодець, ви вгадали число!')
            res = 'Сьогодні гарний день, вам щастить!'
            break
        elif number_random > number_user:
            print('Ваше число замале! Спробуйте ще раз.')
        else:
            print('Ваше число завелике! Спройбуте ще раз.')
        number_user = user()
        allempt += 1
    else:
        res = 'Нажаль спроби закінчились. Пощастить наступного разу!'
    return res


number_random = randint(1, 10)
number_user = user()
res = work(number_user)
print(res)
