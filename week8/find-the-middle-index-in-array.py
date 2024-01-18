class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ps=[0]*(len(nums)+2)
        sm=0
        ans=len(nums)
        flag=False
        for i in range(len(nums)):
            sm+=nums[i]
            ps[i+1]=sm
        for i in range(1,len(ps)-1):
            if ps[len(ps)-2]-ps[i]==ps[i-1]:
                flag=True
                ans=min(ans,i-1)
        if flag:
            return ans
        return -1