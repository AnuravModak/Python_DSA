# bitonic array:A Bitonic Sequence is a sequence of numbers which is first strictly increasing
# then after a point strictly decreasing.Bitonic array is

# now here i need to search an element in bitonic array...so find the peak element after finding the peak element
# apply binary search for ascending order for all the elements to the left of the bitonic point.....
# and apply binary search for descending for all the elemnt to the right of the bitonic point.......

def bs_asc(arr,key):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==key:
            return mid
        if arr[mid]>key:
            end=mid-1
        if arr[mid]<key:
            start=mid+1
    return -1
def bs_desc(arr,key):
    start=0
    end=len(arr)-1
    while end<=start:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            end = mid +1
        if arr[mid] < key:
            start = mid - 1
    return -1

def peak_element(arr):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if mid>0 and mid<len(arr)-1:
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            if arr[mid-1]>arr[mid]:
                end=mid-1
            if arr[mid+1]>arr[mid]:
                start=mid+1
        elif mid==0:
            if arr[0]>arr[1]:
                return 0
            else:
                return 1
        else:
            if arr[len(arr)-1]>arr[len(arr)-2]:
                return len(arr)-1
            else:
                return len(arr)-2
    return -1

def search_element(arr,key):
    peak=peak_element(arr)
    if arr[peak]==key:
        return peak
    y1=bs_asc(arr[0:peak],key)
    y2=bs_desc(arr[peak:],key)
    if y1!=-1:
        return -1
    elif y2!=-1:
        return -1
    else:
        return -1
if __name__ == '__main__':
    bitonic_array=[1,2,3,4,5,6,7,18,16,12,10]
    print(search_element(bitonic_array,11))

