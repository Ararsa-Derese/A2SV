# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=0
        def trv(root,sm):
            if not root:
                return
            nonlocal ans
            sm+=str(root.val)
            trv(root.left,sm)
            trv(root.right,sm)
            if not root.right and not root.left:
                ans+=int(sm)
            
        trv(root,"")
        return ans