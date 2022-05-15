def recrsive_subset(arr,n,s):
    if s==0:
        return True

    if n==0 and s>0:
        return False

    if arr[n-1]>s:
        return recrsive_subset(arr,n-1,s)
    if arr[n-1]<=s:
        return recrsive_subset(arr,n-1,s-arr[n-1]) or recrsive_subset(arr,n-1,s)

def recursive_equalsumpartition(arr,s):

    if s&1:
        return False

    return recrsive_subset(arr,len(arr),s//2)

def topdown_subset(arr,n,s,t):
    if n==0 and s==0:
        return True
    if n==0 and s>0:
        return False
    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1]>j:
                t[i][j]=False
            else:
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
    return t[n][s]
def nonrecursive_equalsum_partition(arr,s,t):
    if s&1:
        return False
    else:
        return topdown_subset(arr,len(arr),s//2,t)

if __name__ == '__main__':
    arr=[3, 1, 5, 9, 12]
    s=sum(arr)
    print(recursive_equalsumpartition(arr,s))
    n=len(arr)

    t=list(list())
    lis=[False]*(s+1)
    for i in range(n+1):
        t.append(list(lis))

    for i in range(n+1):
        t[i][0]=True
    # print(t)
    print(nonrecursive_equalsum_partition(arr,s,t))

