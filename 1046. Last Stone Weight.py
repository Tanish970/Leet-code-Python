class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)>1):
            stones.sort()
            fir=stones.pop()
            sec=stones.pop()
            if(fir!=sec):
                imp=fir-sec if fir>sec else sec-fir
                stones.append(imp)
            else:
                stones.append(0)
        return stones[0]
 
 #Easy to understand but only faster than 10% among python submission but memory usuage 100% better than python submission. 
