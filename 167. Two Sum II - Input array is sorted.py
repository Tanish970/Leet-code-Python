class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h={}
        for i,num in enumerate(numbers):
            n=target-num
            if n not in h:
                h[num]=i+1
            else:
                return [h[n],i+1]
            
