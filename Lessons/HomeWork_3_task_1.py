a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if (a >= 10 and b < 10):
    a,b = b,a
if (b >= 10 and c < 10):
    b,c = c,b
if (a >= 10 and c < 10):
    a,c = c,a
if (c >= 10 and d < 10):
    c,d = d,c
if (a >= 10 and d < 10):
    a,d = d,a
if (b >= 10 and d < 10):
    b,d = d,b
if (d >= 10 and e < 10):
    d,e = e,d
if (a >= 10 and e < 10):
    a,e = e,a
if (b >= 10 and e < 10):
    b,e = d,e
if (c >= 10 and e < 10):
    c,e = e,c
print(a, b, c, d, e)
