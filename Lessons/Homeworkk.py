#a = int(input())
#for i in range(1, a + 1)
#    if a % i == 0:
#        print(i)
p = 8
for i in range(2000, 3660):
    j = []
    for h in range(1, i + 1):
        if i % h == 0:
            j.append(h)
    if p not in j:
        print(i)

