from collections import defaultdict 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=defaultdict(int)
        le=len(nums)
        for i in nums:
            d[i]+=1
            if(d[i]>int(le/2)):
                return i
          
            
        
