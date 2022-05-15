def mah(arr):
    # step-1 find nearest smaller element to the right
    right_ans = []
    stack = []
    # i have carried out this technique necaue our right array will have ans in another format
    arr.append(-1)

    for i in range(len(arr) - 1, -1, -1):
        if len(stack) == 0:
            right_ans.append(-1)
        elif len(stack) > 0 and arr[i] <= arr[stack[-1]]:
            while len(stack) > 0 and arr[i] <= arr[stack[-1]]:
                stack.pop(len(stack) - 1)
            if len(stack) == 0:
                right_ans.append(-1)
            else:
                right_ans.append(stack[-1])

        elif len(stack) > 0 and arr[i] > arr[stack[-1]]:
            right_ans.append(stack[-1])
        stack.append(i)
    right_ans.reverse()

    # step-2: find nearest smaller element to the left
    stack.clear()
    left_ans = []
    for i in range(len(arr)):
        if len(stack) == 0:
            left_ans.append(-1)
        elif len(stack) > 0 and arr[i] <= arr[stack[-1]]:
            while len(stack) > 0 and arr[i] <= arr[stack[-1]]:
                stack.pop(len(stack) - 1)
            if len(stack) == 0:
                left_ans.append(-1)
            else:
                left_ans.append(stack[-1])
        elif len(stack) > 0 and arr[i] > arr[stack[-1]]:
            left_ans.append(stack[-1])
        stack.append(i)

    arr.pop(-1)
    right_ans.pop(-1)
    left_ans.pop(-1)

    #  width=right-left-1
    width = []
    for i in range(len(arr)):
        width.append(right_ans[i] - left_ans[i] - 1)

    #  calulating area
    area = []
    for i in range(len(arr)):
        area.append(width[i] * arr[i])
    return max(area)

def solve(matrix):
    temp=matrix[0].copy()
    max_area=mah(temp)
    n=len(matrix)
    m=len(matrix[0])


    for i in range(1,n):
        for j in range(m):
            if matrix[i][j]==0:
                temp[j]=0
            else:
                temp[j]=temp[j]+matrix[i][j]
        max_area=max(max_area,mah(temp))
    return max_area


