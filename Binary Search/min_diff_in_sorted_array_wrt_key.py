# Here key is given as an input
# now here as the key is given...so if i need to do absolute difference between that key with every element to and get the minimum out of it
# Now here it has two cases:
#  if key is present in array return 0....if it doesnt exist do the absolute diff between floor and ceiling and return the minimum
def ceiling(arr,ele):
    start=0
    end=len(arr)-1
    res=-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==ele:
            return ele
        if arr[mid]>ele:
            res=arr[mid]
            end=mid-1
        if arr[mid]<ele:
            start=mid+1
    return res
def binary_search(arr,ele):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==ele:
            return mid
        if arr[mid]>ele:
            end=mid-1
        if arr[mid]<ele:
            start=mid+1
    return -1
def floor(arr,ele):
    start=0
    end=len(arr)-1
    res=-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==ele:
            return ele
        if arr[mid]>ele:
            end=mid-1
        if arr[mid]<ele:
            res = arr[mid]
            start=mid+1
    return res

def min_element(arr,key):
    y=binary_search(arr,key)
    if y!=-1:
        return 0
    else:
        Floor=floor(arr,key)
        Ceiling=ceiling(arr,key)
        if Floor==-1:
            return abs(key-Ceiling)
        elif Ceiling==-1:
            return abs(key-Floor)
        else:
            return min(abs(key-Floor),abs(key-Ceiling))



if __name__ == '__main__':
    arr = [ 1, 5, 5, 6, 8,9,11,12,15,19]
    print(min_element(arr,13))


