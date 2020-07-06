class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        if len(nums)==1:return nums[0]
        h=[0]*len(nums)
        h[0]=nums[0]
        h[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            h[i]=max(nums[i]+h[i-2],h[i-1])
        return h[-1]
