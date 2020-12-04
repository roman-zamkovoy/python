a = int(input())
c = 0
for i in range(1, a, 1):
    if i % 3 == 0:
        print(i, end = " ")
        c = c + i
print(c)
