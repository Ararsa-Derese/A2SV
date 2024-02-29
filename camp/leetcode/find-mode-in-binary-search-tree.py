# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic=defaultdict(int)
        def trv(root):
            if not root:
                return 
            dic[root.val]+=1
            trv(root.left)
            trv(root.right)
        trv(root)
        a=sorted(dic.values(),reverse=True)
        b=a[0]
        print(a)
        ans=[]
        for key,val in dic.items():
            if val==b:
                ans.append(key)
        return ans