class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:return True
        def arr(node1,node2):
            if not node1 and not node2:return True
            if not node1 or not node2:return False
            if node1.val==node2.val:
                return arr(node1.left,node2.right) and arr(node1.right,node2.left)
            else:return False
        return arr(root,root)
        
