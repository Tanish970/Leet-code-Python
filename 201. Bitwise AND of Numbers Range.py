class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m==0 or n==0:
            return 0
        bot=int(math.log(m,2))
        top=int(math.log(n,2))
        if(top!=bot):return 0
        res=m
        for i in range(m+1,n+1):
            res=res&i
        return res
