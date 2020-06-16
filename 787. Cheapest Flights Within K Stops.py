
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src==dst:
            return 0
        loc=collections.defaultdict(list)
        prices=collections.defaultdict(lambda:float('inf'))
        for w,x,y in flights:
            loc[w]+=[(x,y)]
        q=[(src,-1,0)]
        
        while len(q)>0:
            
            pos,k,cost=q.pop(0)
            if pos==dst or k==K:
                continue
            for neigh,p in loc[pos]:
                
                if cost+p>=prices[neigh]:
                    continue
                else:
                    prices[neigh]=cost+p
                    q+=[(neigh,k+1,cost+p)]
                    
            
        if prices[dst]<float('inf'):return prices[dst]
        return -1
            
                             
                
            
        
                
