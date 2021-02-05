a = [12, 98, 0, -100, 30, -15, -2, 13, 0]

l1 = 0
l2 = 0
for i in a:
    if (i > 0 ):
        l1 = l1 + i
    if (i < 0):
        l2 = l2 + i

print(l1, l2)
