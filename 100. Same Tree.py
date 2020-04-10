class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if(p and q):
            return(p.val==q.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        elif(not p and not q):
            return True
        else:
            return False
        
