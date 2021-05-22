a = [[1,2,3],[3,2,2],[1,2,1]

def print_m(a):
  for i in range(len(a)):
    for j in range(len(a)):
        if (a[i][j] % 2 == 0):
            a[i][j] += a[i][j] + 1
        elif (a[i][j] % 2 != 0):
            a[i][j] -= a[i][j] - 1
    print(a[i][j], end=" ")
print()
print_m(a)