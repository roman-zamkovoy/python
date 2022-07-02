a, b = map(int, input().split())
i = input()
c = a * b
d = c - (c / 100) * 13
if i == 'USD':
    print(d)
elif i == 'RUB':
    print('RUB:', d)
    print('USD:', d / 83.5)
if i == 'EUR':
    print('EUR:', d)
    v = d / 0.93
    print('USD:', v)