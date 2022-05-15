# def cpFact( A, B):
#     lis = []
#
#     def gcd(a, b):
#         if b == 0:
#             return a
#         return gcd(b, a % b)
#
#     while gcd(A, B) != 1:
#         print(A)
#         A = A / gcd(A, B)
#     return int(A)

def multiply(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(A,n):
    if n==0:
        return 1
    m=power(A,n//2)
    if n%2==0:
        return m*m
    else:
        return A*m*m



print(power(3,5))
print(3**5)

import numpy as np

def mat(A):
    by = 10 ** 9 + 7
    if A in [1, 2]:
        return 1


    M = np.matrix([[1, 1], [1, 0]], dtype=int)

    def ret(N):
        if N == 1:
            return M
        M1 = ret(N // 2)
        return (M1 * M1 * M) % by if N % 2 else (M1 * M1) % by

    return np.array(ret(A - 1))[0][0]

M = np.matrix([[1, 1], [1, 0]], dtype=int)
print(M[0][1])
print(M**2)