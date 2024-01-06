class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        x=0
        ans=-float('inf')
        for i in range(len(nums)):
            x+=nums[i]
            if (i-l)+1==k:
                ans=max(ans,x/k)
                x-=nums[l]
                l+=1
                
        return ans
