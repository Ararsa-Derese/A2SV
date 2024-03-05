# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic=defaultdict(list)
        def rec(root,n,c):
            if not root.left and not root.right:
                return 
            if root.left:
                dic[c].append((2*n)+1)
                rec(root.left,(2*n)+1,c+1)
            if root.right:
                dic[c].append((2*n)+2)
                rec(root.right,(2*n)+2,c+1)
        rec(root,0,0)
        print(dic)
        ans=1
        for key, val in dic.items():
            ans=max(ans,(val[-1]-val[0])+1)
        return ans