a = [ ["_","_","_"], ["_","_","_"],  ["_","_","_"]]
robot = [1, 2, 3, 4, 5, 6, 7, 8, 9]
import random

def lose(a):
    for i in range(3):
        if (a[i][0] == "x" and a[i][1] == "x" and a[i][2] == "_"):  # СТРОКа
            return 1
        if (a[i][0] == "x" and a[i][2] == "_" and a[i][2] == "x"):  # СТРОКа
            return 1
        if (a[i][1] == "_" and a[i][2] == "x" and a[i][2] == "x"):  # СТРОКа
            return 1
    # ДЗ - сделать такую же проверку по столбцам и _ДИАГОНАЛИ_

def win (a):
    if (a[0][0] == a[0][1] and a[0][1] == a[0][2]):  # СТРОКИ
        if (a[0][0] == 'x'):
            print("Игрок 1 ПОБЕДИЛ!")
            return 1
        elif (a[0][2] == 'O'):
            print("БАРСИК ПОБЕДИЛ!")
            return 1

    if (a[1][0] == a[1][1] and a[1][1] == a[1][2]):
        if (a[1][0] == 'x'):
            print("Игрок 1 ПОБЕДИЛ!")
            return 1
        elif (a[1][2] == 'O'):
            print("БАРСИК ПОБЕДИЛ!")
            return 1
    if (a[2][0] == a[2][1] and a[2][1] == a[2][2]):
        if (a[2][0] == 'x'):
            print("Игрок 1 ПОБЕДИЛ!")
            return 1
        elif (a[2][2] == 'O'):
            print("БАРСИК ПОБЕДИЛ!")
            return 1
    if (a[0][0] == a[1][1] and a[1][1] == a[2][2]):  # ДИАГОНАЛИ
        if (a[0][0] == 'x'):
            print("Игрок 1 ПОБЕДИЛ!")
            return 1
        elif (a[2][2] == 'O'):
            print("БАРСИК ПОБЕДИЛ!")
            return 1
    if (a[0][2] == a[1][1] and a[1][1] == a[2][0]):
        if (a[0][2] == 'x'):
            print("Игрок 1 ПОБЕДИЛ!")
            return 1
        elif (a[0][2] == 'O'):
            print("БАРСИК ПОБЕДИЛ!")
            return 1
    if (a[0][0] == a[1][0] and a[1][0] == a[2][0]):  # СТОЛБЦЫ
        if (a[0][0] == 'x'):
            print("Игрок 1 ПОБЕДИЛ!")
            return 1
        elif (a[1][0] == 'O'):
            print("БАРСИК ПОБЕДИЛ!")
            return 1
    if (a[0][1] == a[1][1] and a[1][1] == a[2][1]):
        if (a[0][1] == 'x'):
            print("Игрок 1 ПОБЕДИЛ!")
            return 1
        elif (a[1][1] == 'O'):
            print("БАРСИК ПОБЕДИЛ!")
            return 1
    if (a[0][2] == a[1][2] and a[1][2] == a[2][2]):
        if (a[0][2] == 'x'):
            print("Игрок 1 ПОБЕДИЛ!")
            return 1
        elif(a[0][2] == 'O'):
            print("БАРСИК ПОБЕДИЛ!")
            return 1
    return 0


for k in range(4):
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
    robot.remove(n+1)

    for i in range(len(a)):
        for x in range(len(a[i])):
            print(a[i][x],end = " ")
        print()

    if(win(a) == 1):
        exit()
    print("Ходит БАРСИК...")
    hod = random.choice(robot)
    if(lose(a) == 1):
        hod =
    hod = hod - 1
    print(hod + 1)
    a[hod//3][hod%3] = "O"
    robot.remove(hod + 1)
for i in range(len(a)):
    for x in range(len(a[i])):
        print(a[i][x],end = " ")
    print()
if(win(a) == 1):
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
        print(a[i][x], end=" ")
    print()
if (win(a) == 1):
    exit()














































































































