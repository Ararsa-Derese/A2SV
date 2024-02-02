class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        a=set(nums)
        dic={}
        l=0
        ans=0
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
            while len(dic)==len(a):
                dic[nums[l]]-=1
                if dic[nums[l]]==0:
                    del dic[nums[l]]
                l+=1
                ans+= (len(nums)-i)
           
        return ans