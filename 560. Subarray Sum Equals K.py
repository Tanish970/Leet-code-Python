from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s=0
        subarray=defaultdict(int)
        tot=0
        for i in nums:
            s+=i
            if(s==k):
                tot+=1
            if(s-k in subarray):
                tot+=subarray[s-k]
            subarray[s]+=1
        return tot
        
