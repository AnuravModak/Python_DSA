for t in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split()))
    arr.sort()
    s=arr[0]
    for i in range(1,len(arr)):
        s+=arr[i]
    print(s+sum(arr)-arr[0])



