q = [13,-3,7,-2,5,-9,5,6,7]

k = 0
l = 0
for i in q:
    if i > 0:
        k = k + 1
    if i < 0:
        l = l + 1
print(k,l)