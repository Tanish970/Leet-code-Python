class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            j=i+1
            while(j<len(nums)):
                if(target==(nums[i]+nums[j])):
                    return([i,j])
                j+=1
