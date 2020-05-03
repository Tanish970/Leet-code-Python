class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root :return []
        res=[]
        return self.dfs(root,'',res)
    def dfs(self,root,path,res):
        if not root.left and not root.right:
            path=path+str(root.val)
            res.append(path)
            return res
        if root.left:
            self.dfs(root.left,path+str(root.val)+'->',res)
        if root.right:
            self.dfs(root.right,path+str(root.val)+'->',res)
        return res
