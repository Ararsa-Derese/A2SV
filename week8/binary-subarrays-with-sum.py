class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic={}
        sum=0
        dic[sum]=1
        ans=0
        for n in nums:
            sum+=n
            if sum-goal in dic:
                ans+=dic[sum-goal]
            if sum in dic:
                dic[sum]+=1
            else:
                dic[sum]=1
        return ans