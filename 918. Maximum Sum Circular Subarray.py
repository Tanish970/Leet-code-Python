class Solution(object):
    def maxSubarraySumCircular(self, A):
        k=self.kadane(A)
        su=0
        for i in range(len(A)):
            su+=A[i]
            A[i]=-A[i]
        su+=self.kadane(A)
        if su>k and su!=0:return su
        return k
    def kadane(self,A):
        maxloc=maxglo=A[0]
        for i in range(1,len(A)):
            maxloc=max(A[i],A[i]+maxloc)
            if maxloc>maxglo:
                maxglo=maxloc
        return maxglo
        
