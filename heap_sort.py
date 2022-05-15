def heapify(arr):
    i=len(arr)-1
    while i>=0:
        if 2*i+1<=len(arr)-1:
            j=i
            while 2*j+1>=1 and 2*j+1<=len(arr)-1:
                if 2*j+2<=len(arr)-1:
                    temp=max(arr[2*j+1],arr[2*j+2])
                    ind=arr.index(temp)
                    if arr[ind]>arr[j]:
                        arr[j],arr[ind]=arr[ind],arr[j]
                    j=ind

                elif 2*j+1<=len(arr)-1:
                    if arr[2*j+1]>arr[j]:
                        arr[2*j+1],arr[j]=arr[j],arr[2*j+1]
                    j=2*j+1
        i-=1

    return arr
# sort using heap deletion inplace sorting:
def heap_sort(arr):
    i=0
    res=[]
    arr=heapify(arr)
    while i<=len(arr)-1:
        arr[0],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[0]
        j=0
        i += 1
        # print(arr)
        while 2 * j + 1 >= 1 and 2 * j + 1 <= len(arr) - 1-i:
            if 2 * j + 2 <= len(arr) - 1 - i:
                temp = max(arr[2 * j + 1], arr[2 * j + 2])
                ind = arr.index(temp)
                if arr[ind] > arr[j]:
                    arr[j], arr[ind] = arr[ind], arr[j]
                j = ind

            elif 2 * j + 1 <= len(arr) - 1 - i:
                if arr[2 * j + 1] > arr[j]:
                    arr[2 * j + 1], arr[j] = arr[j], arr[2 * j + 1]
                j = 2 * j + 1



    print(arr)















if __name__ == '__main__':
    arr=[10,20,15,12,40,25,18]
    heap_sort(arr)

    



















