for _ in range(int(input())):
    n,m=list(map(int, input().split()))
    arr=list(map(int,input().split()))
    arr.sort()
    ans=0
    mex=1
    for i in arr:
        if i==m:
            continue
        if i==mex:
            mex+=1
        ans+=1
    if mex!=m:
        print(-1)
    elif ans==0:
        print(-1)
    else:
        print(ans)


