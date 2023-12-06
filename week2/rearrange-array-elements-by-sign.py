class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        ng=[]
        ans=[]
        for n in nums:
            if n>0:
                p.append(n)
            else:
                 ng.append(n)
        for i in range(len(p)):
            ans.append(p[i])
            ans.append(ng[i])
        return ans