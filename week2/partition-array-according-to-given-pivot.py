class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ng=[]
        nl=[]
        nq=[]
        ans=[]
        for n in nums:
            if n<pivot:
                nl.append(n)
            elif n==pivot:
                nq.append(n)
            else:
                ng.append(n)
        for l in nl:
            ans.append(l)
        for q in nq:
            ans.append(q)
        for g in ng:
            ans.append(g)
        return ans 