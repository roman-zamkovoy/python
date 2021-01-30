a = int(input())
s = 0
for i in range(1, a, 1):
    print(i,end='+')
    s = s + i
print(a,end = "=")
print(s + a)
