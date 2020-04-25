class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans=ListNode(0)
        dup=ans
        while(l1!=None and l2!=None):
            if(l1.val<l2.val):
                dup.next=l1
                dup=dup.next
                
                l1=l1.next
            else:
                dup.next=l2
                dup=dup.next
                l2=l2.next
            
            
        if(l1!=None):dup.next=l1
        if(l2!=None):dup.next=l2
        return ans.next
        
                
