a = [[1,2,3],[3,2,2],[1,2,1]]

def print_m(a):
  for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j] + 1, end=" ")
    print()
print_m(a)