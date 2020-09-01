#Martix_multiply
import numpy as np

def mtx_multiply(a, b):
    m = len(a)
    n = len(b[1])

    p = n
    C = np.zeros((m,n))
    for i in range(0, m):
        for j in range(0, p):
            suma = 0
            for k in range(0, n):
                suma = suma + A[i][k]*B[k][j]
            C[i][j] = suma

    return C

A = [[1, 2, 3],
     [3, 2, 1],
     [2, 1, 3]]
B = [[3, 2],
    [1, 1],
    [4, 1]]
C=mtx_multiply(A, B)
print(C)

