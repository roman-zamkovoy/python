a = [ ["_","_","_"], ["_","_","_"],  ["_","_","_"]]




def win (a):
    if (a[0][0] == a[0][1] and a[0][1] == a[0][2]):  # СТРОКИ
        if (a[0][0] == 'x'):
            print("Игрок 1 ПОБЕДИЛ!")
            return 1
        elif (a[0][2] == 'O'):
            print("Игрок 2 ПОБЕДИЛ!")
            return 1

    if (a[1][0] == a[1][1] and a[1][1] == a[1][2]):
        if (a[1][0] == 'x'):
            print("Игрок 1 ПОБЕДИЛ!")
            return 1
        elif (a[1][2] == 'O'):
            print("Игрок 2 ПОБЕДИЛ!")
            return 1
    if (a[2][0] == a[2][1] and a[2][1] == a[2][2]):
        if (a[2][0] == 'x'):
            print("Игрок 1 ПОБЕДИЛ!")
            return 1
        elif (a[2][2] == 'O'):
            print("Игрок 2 ПОБЕДИЛ!")
            return 1
    if (a[0][0] == a[1][1] and a[1][1] == a[2][2]):  # ДИАГОНАЛИ
        if (a[0][0] == 'x'):
            print("Игрок 1 ПОБЕДИЛ!")
            return 1
        elif (a[2][2] == 'O'):
            print("Игрок 2 ПОБЕДИЛ!")
            return 1
    if (a[0][2] == a[1][1] and a[1][1] == a[2][0]):
        if (a[0][2] == 'x'):
            print("Игрок 1 ПОБЕДИЛ!")
            return 1
        elif (a[0][2] == 'O'):
            print("Игрок 2 ПОБЕДИЛ!")
            return 1
    if (a[0][0] == a[1][0] and a[1][0] == a[2][0]):  # СТОЛБЦЫ
        if (a[0][0] == 'x'):
            print("Игрок 1 ПОБЕДИЛ!")
            return 1
        elif (a[1][0] == 'O'):
            print("Игрок 2 ПОБЕДИЛ!")
            return 1
    if (a[0][1] == a[1][1] and a[1][1] == a[2][1]):
        if (a[0][1] == 'x'):
            print("Игрок 1 ПОБЕДИЛ!")
            return 1
        elif (a[1][1] == 'O'):
            print("Игрок 2 ПОБЕДИЛ!")
            return 1
    if (a[0][2] == a[1][2] and a[1][2] == a[2][2]):
        if (a[0][2] == 'x'):
            print("Игрок 1 ПОБЕДИЛ!")
            return 1
        elif(a[0][2] == 'O'):
            print("Игрок 2 ПОБЕДИЛ!")
            return 1
    return 0


for i in range(len(a)):
    for x in range(len(a[i])):
        print(a[i][x],end = " ")
    print()
print("Игрок 1 ходит")
n = int(input())
while n > 9 or n < 1:
    print("Введите число от 1 до 9")
    n = int(input())

n = n-1
while a[n//3][n%3] != "_":
    print("Упс,место уже занято выберите другую клетку")
    n = int(input()) -1
a[n//3][n%3] = "x"

for i in range(len(a)):
    for x in range(len(a[i])):
        print(a[i][x],end = " ")
    print()

if(win(a) == 1):
    exit()

print("Игрок 2 ходит")
n = int(input())
while n > 9 or n < 1:
    print("Введите число от 1 до 9")
    n = int(input())

n = n-1
while a[n//3][n%3] != "_":
    print("Упс,место уже занято выберите другую клетку")
    n = int(input()) -1
a[n//3][n%3] = "O"

for i in range(len(a)):
    for x in range(len(a[i])):
        print(a[i][x],end = " ")
    print()

if (win(a) == 1):
    exit()

print("Игрок 1 ходит")
n = int(input())
while n > 9 or n < 1:
    print("Введите число от 1 до 9")
    n = int(input())

n = n-1
while a[n//3][n%3] != "_":
    print("Упс,место уже занято выберите другую клетку")
    n = int(input()) -1
a[n//3][n%3] = "x"

for i in range(len(a)):
    for x in range(len(a[i])):
        print(a[i][x],end = " ")
    print()

if (win(a) == 1):
    exit()

print("Игрок 2 ходит")
n = int(input())
while n > 9 or n < 1:
    print("Введите число от 1 до 9")
    n = int(input())

n = n-1
while a[n//3][n%3] != "_":
    print("Упс,место уже занято выберите другую клетку")
    n = int(input()) -1
a[n//3][n%3] = "O"

for i in range(len(a)):
    for x in range(len(a[i])):
        print(a[i][x],end = " ")
    print()

if (win(a) == 1):
    exit()

print("Игрок 1 ходит")
n = int(input())
while n > 9 or n < 1:
    print("Введите число от 1 до 9")
    n = int(input())

n = n-1
while a[n//3][n%3] != "_":
    print("Упс,место уже занято выберите другую клетку")
    n = int(input()) -1
a[n//3][n%3] = "x"

for i in range(len(a)):
    for x in range(len(a[i])):
        print(a[i][x],end = " ")
    print()

if (win(a) == 1):
    exit()

print("Игрок 2 ходит")
n = int(input())
while n > 9 or n < 1:
    print("Введите число от 1 до 9")
    n = int(input())

n = n-1
while a[n//3][n%3] != "_":
    print("Упс,место уже занято выберите другую клетку")
    n = int(input()) -1
a[n//3][n%3] = "O"

for i in range(len(a)):
    for x in range(len(a[i])):
        print(a[i][x],end = " ")
    print()

if (win(a) == 1):
    exit()

print("Игрок 1 ходит")
n = int(input())
while n > 9 or n < 1:
    print("Введите число от 1 до 9")
    n = int(input())

n = n-1
while a[n//3][n%3] != "_":
    print("Упс,место уже занято выберите другую клетку")
    n = int(input()) -1
a[n//3][n%3] = "x"

for i in range(len(a)):
    for x in range(len(a[i])):
        print(a[i][x],end = " ")
    print()

if (win(a) == 1):
    exit()

print("Игрок 2 ходит")
n = int(input())
while n > 9 or n < 1:
    print("Введите число от 1 до 9")
    n = int(input())

n = n-1
while a[n//3][n%3] != "_":
    print("Упс,место уже занято выберите другую клетку")
    n = int(input()) -1
a[n//3][n%3] = "O"

for i in range(len(a)):
    for x in range(len(a[i])):
        print(a[i][x],end = " ")
    print()

if (win(a) == 1):
    exit()

print("Игрок 1 ходит")
n = int(input())
while n > 9 or n < 1:
    print("Введите число от 1 до 9")
    n = int(input())

n = n-1
while a[n//3][n%3] != "_":
    print("Упс,место уже занято выберите другую клетку")
    n = int(input()) -1
a[n//3][n%3] = "x"

for i in range(len(a)):
    for x in range(len(a[i])):
        print(a[i][x],end = " ")
    print()

if (win(a) == 1):
    exit()
else:
    print("НИЧЬЯ, никто не выйграл.")