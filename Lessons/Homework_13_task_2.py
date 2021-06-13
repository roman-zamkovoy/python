a = [[1,2,3,5],[3,2,2,8],[1,2,1,7],[2,7,5,3]]

for i in range(len(a)):
  for j in range(len(a)):
    if(i < j):
      a[i][j] *= -1
def print_m(a):
  for i in range(len(a)):
    for j in range(len(a)):
        print('{:3}'.format(a[i][j]), end=" ")
    print()
print_m(a)