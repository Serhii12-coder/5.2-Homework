while True:
    print("\n Калькулятор. Введіть 'exit' щоб вийти.")

    number1 = input("Введіть перше число: ")
    if number1.lower() == 'exit':
        break

    while not number1.replace('.', '', 1).isdigit():
        number1 = input("Введіть коректне число: ")

    result = float(number1)

    while True:
        operation = input("Введіть операцію (+, -, *, /) або 'exit': ")
        if operation == 'exit':
            print(f" результат: {result}")
            break

        if operation not in ['+', '-', '*', '/']:
            print(" Не коректна операція.")
            continue

        number2 = input("Введіть наступне число: ")
        if number2.lower() == 'exit':
            print(f" Кінцевий результат: {result}")
            break

        while not number2.replace('.', '', 1).isdigit():
            number2 = input(" Помилка. Введіть корректне число: ")

        number2 = float(number2)

        if operation == '+':
            result = result + number2
        elif operation == '-':
            result = result - number2
        elif operation == '*':
            result = result * number2
        elif operation == '/':
            if number2 == 0:
                print("Ділення на нуль неможливо.")
                continue
            result = result / number2

        print(f" Поточний результат: {result}")


    again = input("\n Хочете почати заново? (так / ні): ").strip().lower()
    if again != 'так':
        print(" До побачення.")
        break
