def lower_bound(arr,x):
    start,end=0,len(arr)-1
    ans=-1
    while start<end:
        mid=(start+end)//2
        # if x is less than or equal to arr[mid] then search in left subarray
        if x<=arr[mid]:
            end=mid
        else:
            start=mid+1
    if start<len(arr)-1 and arr[start]<x:
        start+=1
    return start
def upper_bound(arr,x):
    start,end=0,len(arr)-1
    while start<end:
        mid=(start+end)//2
        # if
        if x>=arr[mid]:
            start=mid+1
        else:
            end=mid
    if start < len(arr)-1 and arr[start] <= x:
        start += 1
    return start







if __name__ == '__main__':
    arr=[1,2,2,2,2,3,3,4,5,6,6,6,7,8,8,9,9]
    print(lower_bound(arr,9))
    print(upper_bound(arr,9))
