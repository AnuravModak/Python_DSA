def next_element(arr,key):
    start=0
    end=len(arr)-1
    res=-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==key:
            start=mid+1
        if arr[mid]<key:
            start=mid+1
        if arr[mid]>key:
            res=arr[mid]
            end=mid-1
    return res

if __name__ == '__main__':
    arr=['a','b','d','e','f','g','j']
    for i in range(len(arr)):
        arr[i]=ord(arr[i])
    key='f'
    y=next_element(arr,ord(key))
    print("Next element is :",chr(y))



