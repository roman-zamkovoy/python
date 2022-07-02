n, k, s, x = input().split()
n = int(n)
k = int(k)
s = int(s)
x = int(x)
i = 0
while (s != x and i < 1000):
    i += 1
    s = s + k
    if (s > n):
        s = s % n
if (s == x):
    print(i)
else:
    print(-1)