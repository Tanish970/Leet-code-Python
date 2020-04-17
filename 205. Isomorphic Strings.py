from collections import defaultdict 
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ans=defaultdict(str)
        an=defaultdict(str)
        if len(s)!=len(t):return False
        for i in range(len(s)):
            if not ans[s[i]] or ans[s[i]]!=t[i]:ans[s[i]]=ans[s[i]]+t[i]
            if not an[t[i]] or an[t[i]]!=s[i]:an[t[i]]=an[t[i]]+s[i]
        for i in ans:
            if len(ans[i])!=1 :return False
        for i in an:
            if len(an[i])!=1 :return False
            
        return True
 
 #Not a very efficient way to solve the problem.
 #Runtime: 36 ms, faster than 80.16% of Python3 online submissions for Isomorphic Strings.
#Memory Usage: 14 MB, less than 17.50% of Python3 online submissions for Isomorphic Strings.
