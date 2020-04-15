class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=[1]*len(nums)
        left,right=1,1
        for i in range(len(nums)):
            prod[i]*=left
            prod[-1-i]*=right
            left*=nums[i]
            right*=nums[-1-i]
        return prod
