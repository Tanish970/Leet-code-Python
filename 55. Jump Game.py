class Solution:
    def canJump(self, nums: List[int]) -> bool:
        f=0
        for i,n in enumerate(nums):
            if f>=i and i+n>f:
                f=n+i
        return f>=len(nums)-1
        
