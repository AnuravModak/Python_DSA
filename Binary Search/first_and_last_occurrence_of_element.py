#So, there are rules to solve questions for binary search
# First....so if in a question it is given a sorted array...
# they are expecting u to use binary search rather than linear search.....

# so this question will be done by dividing the array into two halves
# so the question is simple...if u are finding the first element...
# then if arr[mid]==ele..then move left...as u need the find the first element from left...and remaining is same
# to find the last position: if arr[mid]==ele...move to right and remaining is same.......
import maths

def first_occurence(arr,ele):
    start=0
    end=len(arr)-1
    first=-1
    while start<=end:
        mid = start+(end -start) // 2
        if arr[mid]==ele:
            first=mid
            end=mid-1
            # print(start,mid)

        elif arr[mid]<ele:
            start=mid+1
        else:
            end=mid-1
    return first
def last_occurence(arr,ele):
    start=0
    end=len(arr)-1
    last=-1
    while start<=end:
        mid=start+(end-start) // 2
        if arr[mid]==ele:
            last=mid
            start=mid+1
        elif arr[mid]<ele:
            start=mid+1
        else:
            end=mid-1
    return last




if __name__ == '__main__':
    # arr=[5, 7, 7, 8, 8, 10]
    arr=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ]
    mid=len(arr)//2
    print(arr)
    print(first_occurence(arr,10))
    print(last_occurence(arr,10))


    # You cana also find the count of an element in sorted array in "log(n)" complexity
    first=first_occurence(arr,10)
    last=last_occurence(arr,10)
    print(first,last)
    if last==first:
        print("Occurrence is 1")
    else:
        print("Occurrence is {}".format(last-first+1))

    








