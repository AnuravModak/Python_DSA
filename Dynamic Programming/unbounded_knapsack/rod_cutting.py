def topdown_unbounded(wt,val,w,n,t):
    if n==0 or w==0:
        return 0
    # if t[n][w]!=-1:
    #     return t[n][w]
    for i in range(1,n+1):
        for j in range(1,w+1):
            if val[i-1]>j:
                t[i][j]=t[i-1][j]
            else:
                t[i][j]=min(val[i-1]+t[i][j-wt[i-1]],t[i-1][j])

    return t

if __name__ == '__main__':
    wt =  [1, 3, 4, 5,  11, 10]
    val = wt.copy()
    w = 17
    n = len(val)

    # memoization

    arr=list(list())
    lis=[9999]*(w+2)

    for i in range(n+1):
        arr.append(list(lis))
    for i in range(n+1):
        arr[i][0]=0
    for j in range(w+1):
        arr[0][j]=0

    print(topdown_unbounded(wt,val,w,n,arr))