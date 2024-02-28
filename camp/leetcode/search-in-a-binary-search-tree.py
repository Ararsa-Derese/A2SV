# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.ans=None
        def trv(root):
            if not root:
                return
            if root.val==val:
                self.ans=root
                return
            elif root.val>val:
                trv(root.left)
            else:
                trv(root.right)
        trv(root)
        return self.ans