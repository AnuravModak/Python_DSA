def recursive_knapsack(wt,val,w,n):
    if n==0 or w==0:
        return 0
    if wt[n-1]>w:
        return recursive_knapsack(wt,val,w,n-1)
    if wt[n-1]<=w:
        return max(val[n-1]+recursive_knapsack(wt,val,w-wt[n-1],n-1),recursive_knapsack(wt,val,w,n-1))


# recursive plus checking whether the value already computed or not......
def memoization_knapsack(wt,val,w,n,t):
    if n==0 or w==0:
        return 0
    elif t[n][w]!=-1:
        return t[n][w]

    elif wt[n-1]>w:
        return memoization_knapsack(wt,val,w,n-1,t)
    elif wt[n - 1] <= w:
        return max(val[n - 1] + memoization_knapsack(wt, val, w - wt[n - 1], n - 1,t),
                       memoization_knapsack(wt, val, w, n - 1,t))

def topdown_knapsack(wt,val,w,n,t):
    for i in range(1,n+1):
        for j in range(1,w+1):
            if wt[i-1]<=j:
                t[i][j]=max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    return t



if __name__ == '__main__':
    wt = [1,3,4,5]
    val = [1,4,5,7]
    w = 7
    n=len(val)

    # recursive
    print(recursive_knapsack(wt,val,w,n))

    # memoization
    arr=list(list())
    lis = [-1] * (w+1)
    for i in range(n+1):
        arr.append(list(lis))
    print(memoization_knapsack(wt,val,w,n,arr))

    # top-down
    t=list(list())
    lis=[-1]*(w+1)
    for i in range(n+1):
        t.append(list(lis))

    for i in range(n+1):
        t[i][0]=0
    for j in range(1,w+1):
        t[0][j]=0

    print(topdown_knapsack(wt,val,w,n,t))










