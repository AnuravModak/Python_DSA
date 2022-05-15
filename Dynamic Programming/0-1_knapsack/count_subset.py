def recursive_countsubset(arr,n,s):
    if s==0:
        return 1
    if n==0 and s>0:
        return 0
    if n>=0 and s==0:
        return 1
    if arr[n-1]>s:
        return recursive_countsubset(arr,n-1,s)
    if arr[n-1]<=s:
        return recursive_countsubset(arr,n-1,s)+recursive_countsubset(arr,n-1,s-arr[n-1])

def topdown_countsum(arr,n,s,t):
    if s==0:
        return 1
    if n==0 and s>0:
        return 0
    if n>=0 and s==0:
        return 1
    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1]>j:
                t[i][j]=t[i-1][j]
            elif arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]]+t[i-1][j]
    return t[n][s]

if __name__ == '__main__':
    arr=[1,5,5,1,11,1]
    s=11
    n=len(arr)

    # recursive.....
    print(recursive_countsubset(arr,len(arr),s))

    t=list(list())
    lis=[0]*(s+1)

    for i in range(n+1):
        t.append(list(lis))
    for i in range(n+1):
        t[i][0]=1
    # print(t)
    print(topdown_countsum(arr,len(arr),s,t))




