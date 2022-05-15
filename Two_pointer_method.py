arr=[1,3,2,5,1,1,2,3]
# target_sum=sum(arr)-2
# target_sum=sum(arr)
# target_sum=0
# target_sum=11
target_sum=8
sum_sub=0


def two_pointer_method(arr,target_sum,sum_sub=0):
    i, j = 0, 1
    co=0
    for i in range(len(arr)):
        while sum(arr[i:j+1]) < target_sum and j+1<=len(arr):
            # print('arr',arr[i:j+1])
            j+=1
            if j==len(arr):
                # print(arr[i:j])
                return arr[i:j]
        if  j+1<=len(arr) and sum(arr[i:j+1]) == target_sum:
            return arr[i:j+1]

    return arr[i:j]
print(two_pointer_method(arr,target_sum))
# Complexity is O(n)...not exactly O(n).....but a little more than O(n)...and way more less than O(n^2)
#