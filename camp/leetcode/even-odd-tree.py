# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        ans=[True]
        dic=defaultdict(list)
        def trv(root,c):
            if not root:
                return
            if c%2 and root.val%2:
                ans[0]=False
            if not c%2 and not root.val%2:
                ans[0]=False
            if dic[c] and (not c%2 and root.val<=
            dic[c][-1]):
                ans[0]=False
            if dic[c] and (c%2 and root.val>=dic[c][-1]):
                ans[0]=False
            dic[c].append(root.val)
            trv(root.left,c+1)
            trv(root.right,c+1)
        trv(root,0)
        return ans[0]