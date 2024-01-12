class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=len(nums)
        x=0
        l=0
        f=0
        for i in range(len(nums)):
            x+=nums[i]
            while l<=i and x>=target:
                ans=min(ans,(i-l)+1)
                f=1
                x-=nums[l]
                l+=1
        if f:
            return ans
        return 0