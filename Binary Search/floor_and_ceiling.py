# floor of an element is defined as: largest element in an arr which is less than given "ele"
# ceiling of an element is defined as:the next biggest element after "ele"
def ceiling(arr,ele):
    start=0
    end=len(arr)-1
    res=-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==ele:
            return mid
        if arr[mid]>ele:
            res=mid
            end=mid-1
        if arr[mid]<ele:
            start=mid+1
    return res
def floor(arr,ele):
    start=0
    end=len(arr)-1
    res=-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==ele:
            return mid
        if arr[mid]>ele:
            end=mid-1
        if arr[mid]<ele:
            res = mid
            start=mid+1
    return res

if __name__ == '__main__':
    arr = [5, 7, 7, 8, 8,10]
    print(ceiling(arr,8))
    print(floor(arr,8))
    print(26%26)
