a = [[1,2,-3,5,4],[3,-2,2,8,3],[-1,-2,-1,7, 2],[2,-7,5,-3, 1],[5, 6, 7, 8, 9]]


for i in range(len(a)):
    for j in range(len(a)):
        if i + j == len(a) - 1 or i == j:
            a[i][j] = 0

def print_m(a):
  for i in range(len(a)):
    for j in range(len(a)):
        print('{:3}'.format(a[i][j]), end=" ")
    print()

print_m(a)