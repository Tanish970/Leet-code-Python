#      "Kandane's Algorithm"

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxcurrent=maxglobel=nums[0]
        for i in range(1,len(nums)):
            maxcurrent=max(nums[i],nums[i]+maxcurrent)
            if(maxcurrent>maxglobel):
                maxglobel=maxcurrent
        return maxglobel
            
