class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        c=0
        l=0
        dic={}
        ans=0
        x=0
        for i in range(len(nums)):
            if nums[i] in dic:
                ans=max(ans,x)
                while nums[l]!=nums[i]:
                    del dic[nums[l]]
                    x-=nums[l]
                    l+=1
                x-=nums[l]
                l+=1
            else:
                dic[nums[i]]=1
            x+=nums[i]
        ans=max(ans,x)
        return ans
                
                