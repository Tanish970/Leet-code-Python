class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p =head
        while p:
            if p.next and p.next.val == p.val:
                p.next= p.next.next
            else:
                p = p.next
                
        return head
