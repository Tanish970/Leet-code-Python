class Solution:
    def canJump(self, nums: List[int]) -> bool:
        f=0
        for i in range(len(nums)):
            if f>=i:
                f=max(f,i+nums[i])
        return f>=len(nums)-1
