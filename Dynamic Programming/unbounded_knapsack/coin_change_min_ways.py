import sys

def min_coinchange(arr,n,s,t):
    for i in range(2,n+1):
        for j in range(1,s+1):
            if arr[i-1]>j:
                t[i][j]=t[i-1][j]
            else:
                t[i][j]=min(1+t[i][j-arr[i-1]],t[i-1][j])
    return t[n][s]

if __name__ == '__main__':
    arr=[3,1,4,8]
    n=len(arr)
    s=5
    t=[[0]*(s+1) for i in range(n+1)]
    for i in range(1,s+1):
        t[0][i]=sys.maxsize-2

    for i in range(1,s+1):
        if i%arr[0]==0:
            t[1][i]=i//arr[0]
        else:
            t[1][i]=sys.maxsize-2

    print(min_coinchange(arr,n,s,t))


