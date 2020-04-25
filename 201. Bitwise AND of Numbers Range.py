class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        count=0
        while(m!=n):
            m=m>>1
            n=n>>1
            count+=1
        return m<<count
    

#Explaination video link
https://www.youtube.com/watch?v=-qrpJykY2gE
