class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:return head
        curnode=head
        prev=None
        while(curnode):
            temp=curnode
            curnode=curnode.next
            temp.next=prev
            prev=temp
        return prev
        
