import numpy as np

def print_m(a):
  for i in range(len(a)):
    for j in range(len(a)):
        print('{:3}'.format(a[i][j]), end=" ")
    print()

def T_2_2(a):
    a[0][1], a[1][0] = a[1][0], a[0][1]

def T_3_3(a):
    a[0][1], a[1][0], a[0][2], a[2][0], a[1][2], a[2][1] = a[1][0], a[0][1], a[2][0], a[0][2], a[2][1], a[1][2]

def det(a):
    return a[0][0] * a[1][1] - a[1][0] * a[0][1]

def umn(a,b):
    return ((np.array(a) @ np.array(b)).tolist())
a = [[15, 2, 1], [3, 2, 0], [0, 5, 0]]
print(np.array(a) @ np.array(a).T)