def merge_sort(arr):
    if len(arr)<=1:
        return 0
    inversion=0
    mid=len(arr)//2
    inversion+=merge_sort(arr[:mid])
    inversion+=merge_sort(arr[mid:])
    inversion+=merge_arr(arr[:mid],arr[mid:],arr)

    return inversion
def merge_arr(left,right,arr):
    i,j,k=0,0,0
    inversion=0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            inversion +=len(left)-i
            j += 1
            k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return inversion
if __name__ == '__main__':
    print(merge_sort([1,2,3,6,5]))







