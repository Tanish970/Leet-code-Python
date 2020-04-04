class Solution(object):
    def getIntersectionNode(self, headA, headB):
        stack_a,stack_b=[],[]
        if(headA==headB):
            return headA
        while headA:
            stack_a.append(headA)
            headA=headA.next
        while headB:
            stack_b.append(headB)
            headB=headB.next
        a=None
        if(stack_a==[] or stack_b==[]):
            return
        if(len(stack_a)==1 and len(stack_b)==1):
            if(stack_a[0]==stack_b[0]):
                return stack_a[0]
            return 
        while True:
            if(stack_a==[] or stack_b==[]):
                return
            if(stack_a[-1]!=stack_b[-1]):
                return a
            a=stack_a[-1]
            if(len(stack_a)!=1):stack_a.pop()
            if(len(stack_b)!=1):stack_b.pop()
            
            
