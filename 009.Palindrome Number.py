class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if(x==x[::-1]):
            return True
        return False
   
#Runtime: 56 ms, faster than 76.29% of Python3 online submissions for Palindrome Number.
#Memory Usage: 13.8 MB, less than 6.50% of Python3 online submissions for Palindrome Number.
