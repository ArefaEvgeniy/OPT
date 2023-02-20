while True:
    input_value = input("ВВедите число: ")
    if not input_value.isdigit():
        print("Вы ввели не число, повторите ввод")
        continue

    print(f"Куб введённого числа = {int(input_value) ** 3}")

    answer = input("Хотите выйти? (Y/Д): ")
    if answer.lower() in {"y", "д"}:
        break
