class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return None
        if(root.left or root.right) and root.val == sum:
            return False
        return self.helper(root,sum)
    def helper(self,root,sum):
        if not root:return False
        if sum-root.val==0 and not (root.right or root.left):
            return True
        return self.helper(root.left,sum-root.val) or self.helper(root.right,sum-root.val)
        
