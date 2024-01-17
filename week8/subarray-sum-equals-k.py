class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic={}
        sum=0
        dic[sum]=1
        ans=0
        for n in nums:
            sum+=n
            if sum-k in dic:
                ans+=dic[sum-k]
            if sum in dic:
                dic[sum]+=1
            else:
                dic[sum]=1
        return ans