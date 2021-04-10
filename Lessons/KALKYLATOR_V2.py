
a = int(input())
b = int(input())
c = input()
if (c == "+"):
    print(a + b)
if (c == "/"):
    if b == 0:
        print("Делить на 0 нельзя")
    else:
        print(a / b)
if (c == "-"):
    print(a - b)
if (c == "*"):
    print(a * b)