def solve(arr):
    ans=[]
    stack=[]
    for i in range(len(arr)):
        if len(stack)==0:
            ans.append(-1)
        elif len(stack)>0 and arr[i]<=arr[stack[-1]]:
            ans.append(stack[-1])
        elif len(stack)>0 and arr[i]>arr[stack[-1]]:
            while len(stack)>0 and arr[i]>arr[stack[-1]]:
                stack.pop(len(stack)-1)
            if len(stack)==0:
                ans.append(-1)
            else:
                ans.append(stack[-1])
        stack.append(i)
    # print(ans)
    for i in range(len(ans)):
        ans[i]=i-ans[i]
    return ans
print(solve([100,80,60,70,60,75,85]))
print(solve([10, 4, 5, 90, 120, 80]))