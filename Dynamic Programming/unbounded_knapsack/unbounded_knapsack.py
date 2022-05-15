def recursive_unbounded(wt,val,w,n):
    if n==0 or w==0:
        return 0

    if val[n-1]>w:
        return recursive_unbounded(wt,val,w,n-1)
    elif val[n-1]<=w:
        return max(val[n-1]+recursive_unbounded(wt,val,w-wt[n-1],n),recursive_unbounded(wt,val,w,n-1))

def memoization_unbounded(wt,val,w,n,t):
    if n==0 or w==0:
        return 0
    if t[n][w]!=-1:
        return t[n][w]
    if val[n-1]>w:
        return memoization_unbounded(wt,val,w,n-1,t)
    elif val[n-1]<=w:
        return max(val[n-1]+memoization_unbounded(wt,val,w-wt[n-1],n,t),memoization_unbounded(wt,val,w,n-1,t))

def topdown_unbounded(wt,val,w,n,t):
    if n==0 or w==0:
        return 0
    if t[n][w]!=-1:
        return t[n][w]
    for i in range(1,n+1):
        for j in range(1,w+1):
            if val[i-1]>j:
                t[i][j]=t[i-1][j]
            else:
                t[i][j]=max(val[i-1]+t[i][j-wt[i-1]],t[i-1][j])

    return t[n][w]



if __name__ == '__main__':
    wt =  [1, 3, 4, 5,  11, 10]
    val = [1, 4, 5, 7, 7,  14]
    w = 17
    n = len(val)
    print(recursive_unbounded(wt,val,w,n))

    # memoization

    arr=list(list())
    lis=[-1]*(w+2)

    for i in range(n+1):
        arr.append(list(lis))
    for i in range(n+1):
        arr[i][0]=0
    for j in range(w+1):
        arr[0][j]=0
    print(memoization_unbounded(wt,val,w,n,arr))
    print(topdown_unbounded(wt,val,w,n,arr))


