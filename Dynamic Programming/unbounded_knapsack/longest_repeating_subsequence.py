def abcd(A):
    n = len(A)
    t = [[0] * (len(A) + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and A[i - 1] == A[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j-1])

    return t

if __name__ == '__main__':
    print(abcd("abba"))
    print(abcd("abab"))