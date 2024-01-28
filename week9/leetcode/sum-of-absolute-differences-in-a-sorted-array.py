class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ps=[0]*(len(nums)+2)
        for i in range(len(nums)):
            ps[i+1]=ps[i]+nums[i]
        ans=[]
        for i in range(len(nums)):
            a=((nums[i]*i-(ps[i]))+(ps[-2]-ps[i+1])-(nums[i]*(len(nums)-i-1)))
            ans.append(a)
        return ans