class Solution(object):
    def removeKdigits(self, num, k):
        if len(num)==k:return "0"
        stack=[]
        j=k
        for i in num:
            while j>0 and stack and stack[-1]>i:
                stack.pop()
                j-=1
            stack.append(i)
        ans="".join(stack[0:len(num)-k]).lstrip("0")
        if len(ans):
            return ans
        return "0"
