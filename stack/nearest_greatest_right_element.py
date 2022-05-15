def solve(arr):
    # 1  3  2  4
    ans=[]
    stack=[]
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            ans.append(-1)
        elif len(stack)>0 and arr[i]<stack[-1]:
            ans.append(stack[-1])
        elif len(stack)>0 and arr[i]>stack[-1]:
            while len(stack)>0 and stack[-1]<arr[i]:
                stack.pop(len(stack)-1)
            if len(stack)==0:
                ans.append(-1)
            else:
                ans.append(stack[-1])
        stack.append(arr[i])
    ans.reverse()
    return ans
arr=[1,3,2,4]
# print(arr[-1])
print(solve(arr))
