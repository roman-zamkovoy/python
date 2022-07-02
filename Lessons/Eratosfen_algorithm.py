def prime(k):
    for i in range(2,k//2+1):
        if(k%i==0):
            return False
    return True


n = int(input())
a = list(range(2, n + 1))
for i in range(2, n + 1):
    if (prime(i) == True):
        print(i)