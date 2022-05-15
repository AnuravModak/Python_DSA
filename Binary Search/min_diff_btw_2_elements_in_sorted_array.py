# As the array is sorted the minimum difference between two elements will
# always be the minimum difference between any 2 consecutive elements in the array...Mow you have to find that consecutive pair
# Now this is the case when key is not given as input......
def min_diff(arr):
    start=0
    end=len(arr)-1
    res=999999999999
    for i in range(len(arr)-1):
        if arr[i+1]-arr[i]<res:
            res=arr[i+1]-arr[i]
    return res

if __name__ == '__main__':
    arr=[1,2,3,6,7,8,9]
    print(min_diff(arr))


