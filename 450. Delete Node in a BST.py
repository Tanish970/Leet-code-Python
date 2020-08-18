# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root==None:return None
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            if root.left==None:
                return root.right
            elif root.right==None:
                return root.left
            else:
                a=self.getsucc(root)
                print(root.val)
                root.val=a.val
                root.right=self.deleteNode(root.right,a.val)
        return root
    def getsucc(self,node):
        b=node.right
        while b!=None and b.left!=None:
            b=b.left
        return b
        
