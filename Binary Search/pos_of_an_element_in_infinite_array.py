def binary_search(arr,key):
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
def pos_element(arr,key):
    if len(arr)==1:
        if arr[0]==key:
            return 0
        else:
            return -1
    else:
        start=0
        end=1
        while key>arr[end]:
            try:
                if arr[end] == key:
                    return end
                if arr[end] < key:
                    start = end
                    end = end * 2
                if arr[end] > key:
                    y = binary_search(arr[start:end], key)
                    if y == -1:
                        return None
                    else:
                        return y + start
            except:
                return None


def first_occurrence(arr,key):
    start=0
    end=len(arr)-1
    res=-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==key:
            res=mid
            end=mid-1
        if arr[mid]>key:
            end=mid-1
        if arr[mid]<key:
            start=mid+1
    return res

def first_occurrence_in_binary_array(arr,key):
    if len(arr)==1:
        if arr[0]==key:
            return 0
        else:
            return -1
    else:
        start=0
        end=1
        res=-1
        while key>arr[end]:
            try:
                if arr[end] < key:
                    start = end
                    end = end * 2
                if arr[end] >= key:
                    y = first_occurrence(arr[start:end], key)
                    if y == -1:
                        return None
                    else:
                        return y + start
            except:
                return None



if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7,8,9,16,17]
    print(pos_element(arr,27))
    binary_array=[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]
    print(first_occurrence_in_binary_array(binary_array,1))