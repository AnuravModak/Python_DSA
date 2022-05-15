# this is a dp problem............
for t in range(int(input())):
    n,m=[int(x) for x in input().split()]
    arr=list(list())
    lis=[0]*m
    for i in range(n):
        arr.append(lis)
    for i in range(m):
        arr[0][i]=1
    for i in range(n):
        arr[i][0]=1
    for i in range(1,n):
        for j in range(1,m):
            arr[i][j]=arr[i][j-1]+arr[i-1][j]
    print(arr[n-1][m-1])