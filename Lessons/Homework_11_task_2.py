a = [[1,2,1],[3,2,2],[0,2,0]]
count = 0

for i in range(len(a)):
  for j in range(len(a)):
    if a[i][j] == 1:
      count += 1
print(count)