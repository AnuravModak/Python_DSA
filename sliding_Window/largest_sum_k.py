arr=[4,1,1,1,2,3,4,5,1,1,5,6,1,0,1,1,2]
# print(len(arr))
def solve(arr,k):
    i=0
    j=1
    s=arr[i]+arr[j]
    ans=None
    while j<len(arr):
        if s==k:
            print(arr[i:j+1])
            if ans:
                if len(ans)<len(arr[i:j+1]):
                    ans=arr[i:j+1].copy()
            else:
                ans=arr[i:j+1]
            i+=1
            j+=1
            s=s-arr[i-1]
            if j==len(arr):
                break
            s=s+arr[j]
        elif s>k:
            while s>k:
                i+=1
                s=s-arr[i-1]
                if i==j:
                    j+=1
                    if j==len(arr):
                        break
                    s+=arr[j]

        elif s<k:
            j+=1
            if j==len(arr):
                break
            s=s+arr[j]
    return ans
print(solve(arr,5))


