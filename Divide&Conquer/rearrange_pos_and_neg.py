def rearrange(arr):
    i=0
    negatives=0
    positives=0
    for i in arr:
        if i<0:
            negatives+=1
        else:
            positives+=1

    if min(positives,negatives)==0:
        return arr
    ind=0
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i],arr[ind]=arr[ind],arr[i]
            ind+=2
    return arr
print(rearrange([2,3,-4,-1,6,-9]))
print(rearrange([-1,2,-30,4,5,6,8,9,-99,-1,-7,36]))