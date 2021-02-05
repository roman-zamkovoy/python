a = [12, 98, -100, 30,-10, 110,0, 44, -2]

k = 0
kk = 0
for i in a:
    if i >= 0:
        k = k + 1
for i in a:
    if i < 0:
        kk = kk + 1
print(k - kk or kk - k)