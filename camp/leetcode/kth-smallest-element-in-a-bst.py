# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        li=[]
        def trv(root):
            if not root:
                return
            trv(root.left)
            li.append(root.val)
            trv(root.right)
        trv(root)
        return li[k-1]