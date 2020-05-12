class Solution(object):
    def singleNonDuplicate(self, nums):
        le=len(nums)
        if le==1:return nums[0]
        for i in range(0,len(nums)-1,2):
            if(nums[i]!=nums[i+1]):return nums[i]
        if le%2!=0:return nums[le-1]
