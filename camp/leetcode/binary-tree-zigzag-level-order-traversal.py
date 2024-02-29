# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic=defaultdict(list)
        def trv(root,c):
            if not root:
                return
            dic[c].append(root.val)
            trv(root.left,c+1)
            trv(root.right,c+1)
        trv(root,0)
        ans=[]
        for key,val in dic.items():
            if not key%2:
                ans.append(val)
            else:
                val.reverse()
                ans.append(val)
        return ans
            