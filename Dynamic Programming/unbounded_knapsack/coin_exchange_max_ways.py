# so in unbounded knapsack....whenever you have to send the count...remove max and or operation
# and do addition anteyyyyyy....

def coinchange_count(arr,n,s,t):
    if s>=0 and n==0:
        return 0
    if s==0 and n>0:
        return 1

    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1]>s:
                t[i][j]=t[i-1][j]
            else:
                t[i][j]=t[i-1][j]+t[i][j-arr[i-1]]
    return t[n][s]


if __name__ == '__main__':
    arr=[5,3,2]
    n=len(arr)
    s=5
    t=[[0]*(s+1) for i in range(n+1)]
    # print(t)
    for i in range(1,n+1):
        t[i][0]=1
    print(coinchange_count(arr,n,s,t))

