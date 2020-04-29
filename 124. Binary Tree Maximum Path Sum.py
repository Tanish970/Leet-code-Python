class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.m=float('-inf')
        def dfs(root):
            if not root:return 0
            left=max(0,dfs(root.left))
            right=max(0,dfs(root.right))
            self.m=max(self.m,left+right+root.val)
            return max(left,right)+root.val
        dfs(root)
        return self.m
 #Explanation link:https://www.youtube.com/watch?v=_wUz0XKQ5JM&t=2s
