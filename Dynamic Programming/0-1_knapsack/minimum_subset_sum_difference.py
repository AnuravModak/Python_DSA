def subset(arr,n,s,t):
    if s == 0 and n >= 0:
        return True
    elif n == 0 and s > 0:
        return False

    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1]>j:
                t[i][j]=t[i-1][j]
            else:
                t[i][j]=t[i-1][j] or t[i-1][j-arr[i-1]]

    return t[n][s]

def min_subset_sum_differnce(arr):
    s=sum(arr)
    t=list(list())
    lis=[False]*(s+1)
    n=len(arr)
    for i in range(n+1):
        t.append(list(lis))
    for i in range(n+1):
        t[i][0]=True

    y=subset(arr,len(arr),s,t)
    halfs=((s//2)+1)
    mini=999999999999

    for i in range(1,halfs):
        if t[n][i]:
            mini=min(mini,s-i*2)

    print(mini)






if __name__ == '__main__':
    arr=[1,6,11,5,4]
    min_subset_sum_differnce(arr)









