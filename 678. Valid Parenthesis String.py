class Solution:
    def checkValidString(self,s):
        close = []
        count = []
        for i in range(len(s)):
            if s[i] == '(':
                close.append(i)
            elif s[i] == ')':
                if close:
                    close.pop()
                elif count:
                    count.pop()
                else:
                    return False
            else:
                count.append(i)
        while(count and close):
            if count[-1]>close[-1]:
                close.pop()
                count.pop()
            else:return False
        if close:return False
        return True
