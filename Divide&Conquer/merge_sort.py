def merge_sort(arr):
    if len(arr)<=1:
        return
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    merge_sort(left)
    merge_sort(right)
    return merge_arr(left,right,arr)

def merge_arr(left,right,arr):
    i,j,k=0,0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
            k+=1
        else :
            arr[k]=right[j]
            j+=1
            k+=1
    while i<len(left) :
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right) :
        arr[k]=right[j]
        j+=1
        k+=1
        
    return arr
if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)





