def maxSubarray(arr,n,m):
    prefix=0
    maxi_prefix=0
    s=set()
    s.add(0)
    for i in range(n):
        prefix=(prefix+arr[i])%m

        maxi_prefix=max(prefix,maxi_prefix)
        # Finding iterator pointing to the first
        # element that is not less than value
        # "prefix + 1", i.e., greater than or
        # equal to this value.
        iter=0
        for j in s:
            if j>prefix:
                iter=j
        if iter:
            maxi_prefix=max(maxi_prefix,prefix-iter+m)
        s.add(prefix)
    return maxi_prefix

arr = [3, 3, 9, 9, 5]
n = 5
m = 7
print(maxSubarray(arr, n, m))