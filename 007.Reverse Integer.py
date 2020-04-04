class Solution(object):
    def reverse(self, x):
        if(x<pow(-2,31) and x>(pow(2,31)-1)):
            return 0
        x=str(x)
        if(x[0]=='-'):
            a=x[0]
            x=x[1:]
            x=x[::-1]
            x=a+x
            x=int(x)
            if(x<pow(-2,31)):
                return 0
            return x
        
        x=x[::-1]
        x=int(x)
        if(x>pow(2,31)-1):
            return 0
        return x
 #This code is done by Tanish 
