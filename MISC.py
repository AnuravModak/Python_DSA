# for i in range(1):
#     # n,k=map(int,input().split())
#     arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#     for i in range(1,len(arr)+1):
#         arr.append(i)
#     res = []
#     fin=[]
#     fin1=[]
#     dict={}
#     for i in range(len(arr) - 1):
#         maxi = max(arr[i] ^ arr[i + 1], arr[i + 1])
#     #     if maxi==arr[i] ^ arr[i + 1]:
#     #         fin1.append(arr[i])
#     #     if maxi==arr[i+1]:
#     #         fin1.append(arr[i+1])
#     #         fin.append(fin1)
#     #         fin1.clear()
#     #     res.append([maxi,arr[i],arr[i+1]])
#     #     if maxi not in dict:
#     #         dict[maxi]=[arr[i],arr[i+1]]
#     #     else:
#     #         dict[maxi] = [arr[i], arr[i + 1]]
#     #
#     # max_xor = max(res)
#     # # print(res)
#     # # print(fin)
#     # # print(dict)
#     # print(dict[max(dict.keys())])
def ascending_bs(arr,b):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==b:
            return mid
        if arr[mid]<b:
            start=mid+1
        if arr[mid]>b:
            end=mid-1
    return -1
def descending_bs(arr,b):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==b:
            return mid
        if arr[mid]>b:
            start=mid+1
        if arr[mid]<b:
            end=mid-1
    return -1

def bitonic_array(arr,b):
    start=0
    end=len(arr)-1
    mid = (start + end) // 2
    while mid<=end:
        # mid = (start + end) // 2
        if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
            a,b=ascending_bs(arr[0:mid+1],b) , descending_bs(arr[mid+1:],b)
            print(arr[0:mid+1],arr[mid+1:])
            if a==-1 and b==-1:
                return -1
            if not a==-1:
                return a
            else:
                return mid+b+1
        if arr[mid]==b:
            return mid
        if arr[mid]>arr[mid-1] and arr[mid]<arr[mid+1]:
            mid+=1
        if arr[mid]<arr[mid-1] and arr[mid]>arr[mid+1]:
            mid=-1

print(bitonic_array([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11 ],12))





