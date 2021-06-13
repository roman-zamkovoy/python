n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for x in b:
    l, r = -1, n
    while l + 1 < r:
        m = (l + r) // 2
        if a[m] <= x:
            l = m
        else:
            r = m
    if r == n or (l>=0 and abs(a[l]-x) <= abs(a[r]-x)):
        print(a[l])
    else:
        print(a[r])






