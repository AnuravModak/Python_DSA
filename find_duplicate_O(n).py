# Given a read only array of n + 1 integers between 1 and n,
# find one number that repeats in linear time using less than O(n) space
# and traversing the stream sequentially O(1) times.

# constraints are important........."Given a read only array of n + 1 integers between 1 and n,"
arr=[1,2,3,1,4,4,5]
slow=arr[0]
fast=arr[arr[0]]
try:
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
        print(slow,fast)
    fast = 0
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
        print(slow, fast)

except:
    print(-1)
