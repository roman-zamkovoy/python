import random
a = random.randint(1, 100)
b = random.randint(1, 100)
c = input()
if (c == "+"):
    print(a + b)
if (c == "/"):
    print(a / b or b / a)
if (c == "-"):
    print(a - b or b - a)
if (c == "*"):
    print(a * b)

print("Сколько хочешь попыток?")
x = int(input())


print('Сколько будет', a , "+", b, "?")
c = int(input())
while(c != a + b and x != 1):
    print("Ответ неверен")
    x = x -1
    print("у вас осталось", x, "попыток")
    c = int(input())

if c == a + b:
    print("Ответ верен 🏆")
else:
    print("Ты проиграл, проверяй знания почаще")












