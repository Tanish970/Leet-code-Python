class Solution(object):
    def oddEvenList(self, head):
        if not head:return None
        odd=ListNode(0)
        even=ListNode(0)
        oddHead=odd
        evenHead=even
        t=1
        while head:
            if t%2:
                odd.next=head
                odd=odd.next
            else:
                even.next=head
                even=even.next
            t+=1
            head=head.next
        even.next=None
        odd.next=evenHead.next
        return oddHead.next
