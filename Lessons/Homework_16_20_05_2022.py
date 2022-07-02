array = list(map(int, input().split()))
number = int(input())
a = 0
b = 0
for i in range(len(array)):
    if array[i] + 1 == number:
        a = array[i]
for i in range(len(array)):
    if array[i] * 2 == number:
        b = array[i]
print(a, b)

