# nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
# dp = [0 for i in range(len(nums))]
# dp[0] = nums[0]
# for i in range(1,len(nums)):
#     dp[i] = max(dp[i-1]+nums[i],nums[i])
#     print(dp)
# print(max(dp))
#


# arr=[1, 34, 3, 98, 9, 76, 45, 4]
# arr=[54, 546, 548, 60]
# str_arr=[]
# for i in arr:
#     str_arr.append(str(i))
# str_arr.sort(key=lambda x:int(x[0]),reverse=True)
# heap=[]
# for i in range(len(arr)-1):
#     s1=arr[i]+arr[i+1]
#     s2=arr[i+1]+arr[i]
#     if int(s1)>int(s2):
#
# # R.sort(key=lambda x:x[1])
# print(str_arr)
A=[0,1, 2, 3]
b=[]
for i in A:
    b.append(str(i))
s=''
s1=int(s.join(b))
nums=int(s1)+1
s1=str(nums)
b.clear()
for i in range(len(s1)):
    if s1[0]=='0':
        pass
    else:
        b.append(s1[i])


print(b)
