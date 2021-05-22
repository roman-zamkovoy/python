count = 0
max = 0  
for i in range(1016, 7938, 1):
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
       count += 1
       if i > max:
           max = i
print(count,max)





