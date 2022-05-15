def countsubset(arr,n,s,t):
    if n==0 and s>0:
        return 0
    if n>=0 and s==0:
        return 1

    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1]>j:
                t[i][j]=t[i-1][j]
            else:
                t[i][j]=t[i-1][j]+t[i-1][j-arr[i-1]]
    return t[n][s]

def count_subset_difference(arr,k):
    s=sum(arr)
    t=list(list())
    target = (k + s) // 2
    lis=[0]*(target+1)
    n=len(arr)

    if n == 0 and s > 0:
        return 0
    if n >= 0 and s == 0:
        return 1
    for i in range(n+1):
        t.append(list(lis))
    for i in range(n+1):
        t[i][0]=1


    return countsubset(arr,n,target,t)

if __name__ == '__main__':
    arr=[1,1,2,3]
    k=1
    print(count_subset_difference(arr,k))


