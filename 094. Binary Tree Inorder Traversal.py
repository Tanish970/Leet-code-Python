class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            if root.left or root.right:
                return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
            else:
                return [root.val]
            
        else:
            return []
