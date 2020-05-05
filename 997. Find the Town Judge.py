class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N==1:return 1
        res=[0]*(N+1)
        p=[]
        for i,j in trust:
            res[j]+=1
            p.append(i)
        m=max(res)
        if m==N-1 and res.index(m) not in p:return res.index(m)
        return -1
