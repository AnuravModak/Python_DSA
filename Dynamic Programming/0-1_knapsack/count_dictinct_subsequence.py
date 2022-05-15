def numDistinct( A, B):
    m=len(A)
    n=len(B)
    dp=list(list())
    arr=[0]*(m+1)
    for i in range(n+1):
        dp.append(list(arr))
    for i in range(m+1):
        dp[0][i]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if B[i-1]==A[j-1]:
                dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
            else:
                dp[i][j]=dp[i][j-1]
    return dp[n][m]



print(numDistinct("aaaababbababbaabbaaababaaabbbaaabbb","bbababa"))