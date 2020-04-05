#Time Complexity O(n)
#Space Complexity O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(t)>500000 or len(s)>100):
            return False
        
        for i in s:
            
            if i in t:
                a=t.index(i)+1
                t=t[a:]
            else:
                return False
        return True
                
                
                
#Runtime: 20 ms, faster than 99.87% of Python3 online submissions for Is Subsequence.
#Memory Usage: 18.4 MB, less than 26.67% of Python3 online submissions for Is Subsequence.
