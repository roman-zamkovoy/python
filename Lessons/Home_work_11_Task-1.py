a = [[1,2,1],[3,2,2],[0,2,0]]

def print_m(a):
  for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j], end=" ")
    print()
print_m(a)