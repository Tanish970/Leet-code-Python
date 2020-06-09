class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        src=sorted(costs,key=lambda x:x[0]-x[1])
        tot=0
        for i in range(len(costs)):
            if i<len(costs)/2:
                tot+=src[i][0]
            else:
                tot+=src[i][1]
        return tot
