class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        rep=[]
        dup=nums
        for i in nums:
            dup=dup[1:]
            if(i not in dup and i not in rep):
                return i
            else:
                rep.append(i)
