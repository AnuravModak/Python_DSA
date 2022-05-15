arr=["a","c","b","c","d","e","e","f","g","g","h","i","j","j","k","l","m","n"]

def solve(arr):
    i=0
    j=1
    n=len(arr)
    ans=None
    while j<n:
        if arr[j] in arr[i:j]:
            if ans:
                if len(ans)<=len(arr[i:j]):
                    ans=arr[i:j].copy()
            else:
                ans=arr[i:j].copy()
            i=j
            j+=1
        else:
            j+=1
    # this statement is important as we are taking arr[i:j] and not arr[i:j+1]

    # if len(arr[i:j])>len(ans):
    #     l=list(dict.fromkeys(arr[i:j+1]))
    #     if len(l)==len(arr[i:j]):
    #         ans=arr[i:j]

    # the last few lines can also be written as: but the time complexity will remain same
    if len(arr[i:j])>len(ans):
        ans=arr[i:j]

    return ans
print(solve(arr))
