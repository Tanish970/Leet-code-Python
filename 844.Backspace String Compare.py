class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s,t=[],[]
        for i in S:
            if(i=='#'):
                if(len(s)!=0):s.pop()
            else:
                s.append(i)
        for i in T:
            if(i=='#'):
                if(len(t)!=0):t.pop()
            else:
                t.append(i)
        return (s==t)
        
