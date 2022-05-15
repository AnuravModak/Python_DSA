res=[]
def helperfunc(m):
    left = 0
    right = len(m) - 1
    ans = 0
    while left < right:
        if not m[left] == m[right]:
            ans += 1
        right -= 1
        left += 1
    return ans
for i in range(int(input())):
    n,k=[int(x) for x in input().split()]
    m=input()
    if n==1:
        res.append("YES")
    else:
        count=helperfunc(m)
        if count<=k:
            # now we lnow that in odd number the middle element is always and palindrome...so whether its 0 or not
            # so when ur count<=k...use the remaining flips to make it fall under palindrome category
            if len(m)%2==1:
                res.append("YES")
            else:
                # now if ur no is even...then the difference between count and
                # flips must be a multiple of 2..else u wont be able to make it palindrom
                if (k-helperfunc(m))%2==0:
                    res.append("YES")
                else:
                    res.append("NO")
        else:
            res.append("NO")

for i in res:
    print(i)