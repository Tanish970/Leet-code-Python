class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                a.append(i)
            if ((a==[]) or (i==')' and a.pop()!='(') or (i==']' and a.pop()!='[') or (i=='}' and a.pop()!='{')):
                return False
            
        if a!=[]:
            return False
        return True




#Runtime: 28 ms, faster than 70.03% of Python3 online submissions for Valid Parentheses.
#Memory Usage: 14 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
