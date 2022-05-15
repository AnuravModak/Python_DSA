# import bisect
# from bisect import bisect_left,bisect_right
#
# # arr=[1,2,0,6,5]
# listOfMarks=[8,7,6,7,8,8,7,6,7,8,9]
# s=listOfMarks.copy()
# s.sort()
# print(s)
# print(bisect_right(s,7))
from bisect import bisect_left


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i:
        return (i - 1)
    else:
        return -1
def solve( A):
    n = len(A)
    dp = [0] * n
    dp[n - 1] = A[n - 1]
    for i in range(n - 2, -1, -1):
        dp[i] = max(dp[i + 1], A[i])
    print(dp)
    lst = []
    maxe = 0
    lst.append(A[0])
    print(A)
    for i in range(1, n - 1):
        res = BinarySearch(lst, A[i])

        if (res != -1):
            if dp[i + 1] <= A[i]:
                continue
            ans = lst[res] + A[i] + dp[i + 1]
            maxe = max(maxe, ans)
        lst.insert(res + 1, A[i])
        print(res, A[i])
        print(lst)
    return maxe

print(solve([1, 5, 9, 1, 4, 3]))
