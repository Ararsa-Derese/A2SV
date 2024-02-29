# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans=-float('inf')
        def trv(root,mn,mx):
            nonlocal ans
            if not root:
                return
            if root.val>mx:
                mx=root.val
            if root.val<mn:
                mn=root.val
            if abs(mx-mn)>ans:
                ans=abs(mx-mn)
            trv(root.left,mn,mx)
            trv(root.right,mn,mx)
        trv(root,float('inf'),-float('inf'))
        return ans
            