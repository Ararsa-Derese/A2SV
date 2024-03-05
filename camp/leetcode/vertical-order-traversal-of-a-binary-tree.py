# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic=defaultdict(list)
        def trv(root,i,j):
            if not root:
                return
            dic[j].append([i,root.val])
            trv(root.left,i+1,j-1)
            trv(root.right,i+1,j+1)
            
        trv(root,0,0)
        li=sorted(dic)
        ans=[]
        for i in range(len(li)):
            dic[li[i]].sort()
            ans.append([j for i,j in dic[li[i]]])
        return ans