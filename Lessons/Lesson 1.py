x = int(input())
if (x >= 0) and x <= 2:
    print('Двойка')
elif (x >= 3) and x < 5:
    print('Тройка')
elif (x >= 5) and x <= 8:
    print('Четвёрка')
elif (x >= 9) and x <= 10:
    print('Пятёрка')
else:
    print("Неправильное число. Введите число от 1 до 10")
