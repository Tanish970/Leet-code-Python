class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:return
        else:
            root.right,root.left=self.invertTree(root.left),self.invertTree(root.right)
        return root
        
