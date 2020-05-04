class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low=1
        high=num//2
        while(low+1<high):
            mid=(low+high)//2
            if mid*mid==num:return True
            elif mid*mid>num:high=mid
            else:low=mid
        return low*low==num or high*high==num
