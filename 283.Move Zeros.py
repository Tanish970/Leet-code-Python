class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        a=0
        b=0
        for i in range(len(nums)):
            if(nums[a]==0):
                nums.pop(a)
                b+=1
            else:
                
                a+=1
        for i in range(b):
            nums.append(0)
        return nums
