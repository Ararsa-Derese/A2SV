# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root.right and not root.left:
            return True
        li=[]
        def trv(root):
            if not root:
                return
            trv(root.left)
            li.append(root.val)
            trv(root.right)
        trv(root)
        for i in range(1,len(li)):
            if li[i]<=li[i-1]:
                return False
        return True