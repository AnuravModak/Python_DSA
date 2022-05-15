# now here you will learn how to find the minimum element in rotated sorted or sorted
# array in "log(n)" complexity.
# to find the minimum element in rotated sorted array...we know to know one thing....
# An unique property => arr[minimum]<arr[next] and arr[minimum]<arr[prev]......
# so how to formulate prev and next.....
# prev=(mid+n-1)%n and next=(mid+1)%n....modulo is only done to prevent the iterator to go out off bounds..
#  now if arr[mid] does not satisfy we will compare "start and mid" and "end and mid"
# now in this case if arr[start]<arr[mid]...which means all the elements from start to mid are in sorted form
# So we need to move to unsorted form

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



def min_element(arr):
    # here i will return index and not the element at that index
    start=0
    end=len(arr)-1
    n=len(arr)
    if arr[start]<arr[end]:
        return 0
    while start<=end:
        if arr[start]<=arr[end]:
            return start
        # means it is soretd so give the first one directly.....
        # else===>

        mid=(start+end)//2
        next=(mid+1)%n
        prev=(mid+n-1)%n
        if arr[mid]<arr[next] and arr[mid]<arr[prev]:
            return mid
        if arr[start]<=arr[mid]:
            start=mid+1
        elif arr[mid]<=arr[end]:
            end=mid-1


def find_pos_of_an_ele(arr,ele):
    y=min_element(arr)
    left=binary_search(arr[:y],ele)
    right=binary_search(arr[y+1:],ele)
    if left !=-1:
        return left
    elif right!=-1:
        return right+len(arr)//2
    else:
        return "Does not exist"




#  now our task is to find the number of rotation done on a sorted array.....
#  and that could be done by getting min element from the given rotated sorted array
if __name__ == '__main__':
    arr=[11,12,15,18,1,5,5,6,8]
    y=min_element(arr)
    print("array is rotated {} times".format(y+1))
    print(find_pos_of_an_ele(arr,5))






















