a = [[1,2,3,2],[1,3,2,2],[1,0,2,1],[1,3,6,9]]

sum = 0
for i in range(len(a)):
  for j in range(len(a)):
    if(i < j):
      sum += a[i][j]
print(sum)