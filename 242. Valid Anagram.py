from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        a,b=defaultdict(int),defaultdict(int)
        for i in 'abcdefghijklmnopqrstuvwxyz':
            a[i]=s.count(i)
            b[i]=t.count(i)
        return a==b
        
