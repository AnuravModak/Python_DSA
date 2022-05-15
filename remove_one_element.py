import collections

for _ in range(int(input())):
    n=int(input())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    arr2.sort()
    arr1.sort()
    maxi=arr1[-1]
    freq=[False]*(maxi+1)
    for i in arr1:
        freq[i]=True
    ans=arr2[0]-arr1[1]
    try:
        for i in arr2:
            if not freq[i - ans]:
                ans = arr2[0] - arr1[0]
                break
        if ans <= 0:
            # ans = arr2[0] - arr1[0]
            if ans==arr2[0]-arr1[1]:
                ans=arr2[0]-arr1[0]
            else:
                ans=arr2[0]-arr1[0]
        print(ans)
    except:
        if ans <= 0:
            # ans = arr2[0] - arr1[0]
            if ans==arr2[0]-arr1[1]:
                ans=arr2[0]-arr1[0]
            else:
                ans=arr2[0]-arr1[0]
        else:
            print(ans)


