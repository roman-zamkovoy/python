a = [[1,2,3,4],[2,3,2,2],[3,1,2,1],[3,8,2,1]]

sum = 0
for i in range(len(a)):
  for j in range(len(a)):
    if(a[i][j] % 2 == 0):
      sum += a[i][j]
print(sum)
