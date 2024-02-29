class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans=0
        if len(nums)==1:
            return True
        for i in range(len(nums)):
            ans=max(ans,i+nums[i])
            if ans==len(nums)-1:
                return True
            if i==ans:
                return False
            
        return True
