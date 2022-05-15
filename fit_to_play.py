for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    prefix=[0]*len(arr)
    prefix[0]=arr[0]
    mini=prefix
    if len(arr)==1:
        print("UNFIT")
    else:
        for i in range(1,len(arr)):
            prefix[i]=min(prefix[i-1],arr[i])
        # print(prefix)
        ans=0
        for i in range(1,len(arr)):
            ans=max(arr[i]-prefix[i],ans)
        if ans==0:
            print("UNFIT")
        else:
            print(ans)

# 3
# 6
# 3 7 1 4 2 4
# 5
# 5 4 3 2 1
# 5
# 4 3 2 2 3