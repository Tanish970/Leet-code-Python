class Solution:
    def isHappy(self, n: int) -> bool:
        if(n==1):
            return True
        if(n<10 and n!=7):
            return False
        sum=0
        while(n!=0):
            a=int(n%10)
            sum=sum+(a*a)
            n=int(n/10)
        return self.isHappy(sum)
           
