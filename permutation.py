
def solve_permute(nums,idx):
    if len(nums)==1:
        return nums
    if idx==len(nums):

        print(nums)


    for i in range(idx,len(nums)):
        nums[i],nums[idx]=nums[idx],nums[i]
        ans=solve_permute(nums,idx+1)
        nums[i], nums[idx] = nums[idx], nums[i]





nums=[1,2,3]

print(solve_permute(nums,0))




