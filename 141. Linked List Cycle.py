class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:return False
        slow,fast=head,head
        while(1):
            if(slow.next==None or fast.next==None or fast.next.next==None):
                return False
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return True
       
#Runtime: 44 ms, faster than 85.53% of Python3 online submissions for Linked List Cycle.
#Memory Usage: 16.9 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
