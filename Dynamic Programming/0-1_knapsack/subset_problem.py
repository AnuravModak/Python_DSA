def recrsive_subset(arr,n,s):
    if s==0 and n>=0:
        return True
    elif n==0 and s>0:
        return False
    elif arr[n-1]>s:
        return False
    elif arr[n-1]<=s:
        return recrsive_subset(arr,n-1,s-arr[n-1]) or recrsive_subset(arr,n-1,s)



def topdown_subset_problem(arr,n,s):
    if s == 0 and n >= 0:
        return True
    elif n == 0 and s > 0:
        return False
    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1]<=s:
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]

    return t







if __name__ == '__main__':
    arr=[2,3,4,5,3]
    s=11
    # arr=[ 35, 54, 100, 19, 39, 1, 89, 28, 68, 29, 94 ]
    # s=649
    # recursive
    print(recrsive_subset(arr,len(arr),s))
    t=list(list())
    n=len(arr)
    lis=[False]*(s+1)
    for i in range(len(arr)+1):
        t.append(list(lis))
    for i in range(n+1):
        t[i][0]=True


    t[0][0]=True
    # print(t)
    print(topdown_subset_problem(arr,n,s))



