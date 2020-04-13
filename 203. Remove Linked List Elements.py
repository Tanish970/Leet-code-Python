class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:return head
        a=head
        while head.next:
            if head.next.val==val:
                head.next=head.next.next
            else:
                head=head.next
        if a.val==val:return a.next
        return a
