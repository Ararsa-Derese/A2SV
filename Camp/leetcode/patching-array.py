class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        target=1
        i=0
        ans=0
        sm=0
        while target <= n:
            if i<len(nums) and target>=nums[i]:
                target+=nums[i]
                i+=1
            else:
                ans+=1
                target*=2
        return ans