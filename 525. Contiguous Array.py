class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        c,d,m = 0,{0:-1},0
        for i,v in enumerate(nums):
            if v==0:c-=1
            if v==1:c+=1
            if c in d:
                l=i-d[c]
                m=max(l,m)
            else:
                d[c]=i
        return m
            
