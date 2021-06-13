a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(a - 5, b, c)
elif b > a and b > c:
    print(a, b - 5, c )
elif b == a and b == c and c == a:
    print("Они все равны")
else:
    print(a, b, c - 5 )

