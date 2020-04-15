import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1 or n==2:
            return 0
        if n==3:
            return 1
        a=[True]*n
        a[0]=False
        a[1]=False
        for i in range(2,int(math.sqrt(n)+1)):
            if a[i]==True:
                for j in range(i*i,n,i):
                    a[j]=False
        return len([i for i in a if i==True])
