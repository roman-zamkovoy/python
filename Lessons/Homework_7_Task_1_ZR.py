a = list(range(41,90,1))
for e in a:
    b =  1
    for i in range(2,e):
        if e % i == 0:
            b = 0
    if(b == 1):
        print(e)