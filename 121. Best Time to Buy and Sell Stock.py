def maxProfit(self, prices: List[int]) -> int:
        curmax=0
        totmax=0
        i=0
        while(prices!=[] and i<(len(prices)-1)):
            if(prices[i]<prices[i+1]):
                curmax=max(prices[i+1:])-prices[i] 
                prices=prices[i+1:]
                totmax=curmax if(curmax>totmax) else totmax
                i=0
            else:i+=1
        return totmax
            
