import numpy as np
lst = input().split()
n = int(lst[0])
a = int(lst[1])
zero = np.zeros((n,), dtype=int)
lst = []
for i in range(0, a):
    queries = list(map(int, input().split()))
    lst.append(queries)
matrix = np.array(lst)

for x in range(0, a):
    for y in range(matrix[x][0]-1, matrix[x][1]):
        zero[y] = zero[y] + matrix[x][2]
    print(zero)

print(np.amax(zero))