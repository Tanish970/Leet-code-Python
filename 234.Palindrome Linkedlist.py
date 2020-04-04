class Solution(object):
    def isPalindrome(self, head):
        a=[]
        while(head):
            a.append(head.val)
            head=head.next
        if(a==a[::-1]):
            return True
        return False
