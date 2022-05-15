# # import math
# # for _ in range(int(input())):
# #     n,k=list(map(int,input().split()))
# #     arr=list(map(int,input().split()))
# #     arr.sort()
# #     count=0
# #     for i in arr:
# #         if i>k:
# #             if math.ceil(i/2)<=k:
# #                 count+=1
# #                 k=k-math.ceil(i/2)
# #             else:
# #                 break
# #         else:
# #             count+=1
# #             k=k-i
# #     print(count)
# #
# #
# #
# a=[1,2,2,2,3,3,4,5,4,2,2]
# print(set(a))

for _ in range(int(input())):
    n=int(input())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    poss=True
    for i in range(n):
        if arr2[i]<arr1[i]:
            poss=False
            print(-1)
            break
    if poss:
        for i in range(len(arr1)):
            arr1[i]=arr2[i]-arr1[i]
        print(arr1)
        suffix_arr=[0]*n
        for i in range(len(arr1)-2,-1,-1):
            if arr1[i]==0:
                continue
            arr1[i]=arr1[i]+arr1[i+1]
        print(arr1)
        print(max(arr1))



# 1
# 5
# 2 3 5 1 2
# 4 3 6 2 3

