class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic={}
        ans=0
        for n in nums:
            if n in dic:
                dic[n]+=1
            else:
                dic[n]=1
        for key,val in dic.items():
            ans+= val*(val-1) // 2
        return ans
