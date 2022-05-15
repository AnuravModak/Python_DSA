# this is tested with test cases and it sucessfully cleared all test cases
def solve(arr):
    # step-1 find nearest smaller element to the right
    right_ans=[]
    stack=[]

    arr.append(-1)
    # i have carried out this technique necaue our right array will have ans in another format
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            right_ans.append(-1)
        elif len(stack)>0 and arr[i]<=arr[stack[-1]]:
            while len(stack)>0 and arr[i]<=arr[stack[-1]]:
                stack.pop(len(stack)-1)
            if len(stack)==0:
                right_ans.append(-1)
            else:
                right_ans.append(stack[-1])

        elif len(stack)>0 and arr[i]>arr[stack[-1]]:
            right_ans.append(stack[-1])
        stack.append(i)
    right_ans.reverse()
    # step-2: find nearest smaller element to the left
    stack.clear()
    left_ans=[]
    for i in range(len(arr)):
        if len(stack)==0:
            left_ans.append(-1)
        elif len(stack) > 0 and arr[i] <= arr[stack[-1]]:
            while len(stack) > 0 and arr[i] <= arr[stack[-1]]:
                stack.pop(len(stack) - 1)
            if len(stack) == 0:
                left_ans.append(-1)
            else:
                left_ans.append(stack[-1])
        elif len(stack)>0 and arr[i]> arr[stack[-1]]:
            left_ans.append(stack[-1])
        stack.append(i)

    arr.pop(-1)
    right_ans.pop(-1)
    left_ans.pop(-1)
    print("arr: ", arr)
    print("right: ",right_ans )
    print("left: ",left_ans )

    #  width=right-left-1
    width=[]
    for i in range(len(arr)):
        width.append(right_ans[i]-left_ans[i]-1)
    print("width: ",width)

    #  calulating area
    area=[]
    for i in range(len(arr)):
        area.append(width[i]*arr[i])
    print("area: ",area)
    return max(area)

hist = [6, 2, 5, 4, 5, 1, 6]
print(solve(hist))




