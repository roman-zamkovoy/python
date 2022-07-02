a, b, c = input().split()
a = int(a)
b = int(b)
for i in range(1, a + 1):
    print(i, 'День:', b * i, c, end='')
    if c == "RUB":
        n = b * i / 83.5
        print(';', round(n, 1), 'USD')
    if c == 'EUR':
        n = (b * i) / 0.93
        print(';', round(n, 1), 'USD')