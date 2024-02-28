# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if (root.val>=p.val and root.val<=q.val) or root.val>=q.val and root.val<=p.val:
            return root
        if root.val>p.val and root.val>q.val:
                ans=self.lowestCommonAncestor(root.left,p,q)
        else:
                ans=self.lowestCommonAncestor(root.right,p,q)
        return ans
        # pp=[]
        # pq=[]
        # def trv(root):
        #     if not root:
        #         return
        #     if root.val==q.val:
        #         pq.append(root.val)
        #         return
        #     pq.append(root.val)
        #     if root.val>q.val:
        #         trv(root.left)
        #     else:
        #         trv(root.right)
        # def trv1(root):
        #     if not root:
        #         return
        #     if root.val==p.val:
        #         pp.append(root.val)
        #         return
        #     pp.append(root.val)
        #     if root.val>p.val:
        #         trv1(root.left)
        #     else:
        #         trv1(root.right)
        # res=[]
        # def rtn(root,target):
        #     if not root:
        #         return
        #     if root.val==target:
        #         res.append(root)
        #         return
        #     if root.val>target:
        #         rtn(root.left,target)
        #     else:
        #         rtn(root.right,target)
        # trv(root)
        # trv1(root)
        # print(pq)
        # print(pp)
        # ans=(list(set(pq) & set(pp)))
        # print(ans)
        # rtn(root,ans[-1])
        # return res[-1]

         
        