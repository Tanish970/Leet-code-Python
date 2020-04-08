class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head or head.next==None:return head
        le=0
        ans=head
        while ans:
            le+=1
            ans=ans.next
        for i in range(0,int(le/2)):
            head=head.next
        return head
            
