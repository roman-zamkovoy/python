a = [12, 98, -100, 30,-10]

s = 0
k = 0
ss = 0
kk = 0
for i in a:
    if i > 0:
        s = s + i
        k = k + 1
for i in a:
    if i < 0:
        ss = ss + i
        kk = kk + 1
print(s/k)
print(ss/kk)