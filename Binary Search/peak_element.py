#  now you only gonna implement code for peak element for bitonic arrays only......

def peak_element(arr):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low +(high-low)//2
        if mid>0 and high<len(arr)-1:
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid-1]>arr[mid]:
                high=mid-1
            else:
                low=mid+1
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

if __name__ == '__main__':
    arr=[5, 6, 7, 8, 9, 10, 3, 2, 1]
    print(peak_element(arr))