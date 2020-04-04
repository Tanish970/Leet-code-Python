class Solution(object):
    def detectCycle(self, head):
        if not head:
            return head
        a=head
        lis=[]
        while a:
            if a in lis:
                return a
            lis.append(a)
            a=a.next
