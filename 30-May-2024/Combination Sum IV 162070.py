# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        def BST_remove_ele_greater_target():
            lo, hi = 0, len(nums) 
            while lo <= hi:
                mid = (lo + hi) // 2
                mid_num = nums[mid]
                if mid_num == target : return nums[:mid+1]
                elif mid_num > target: hi = mid - 1
                else                 : lo = mid + 1
            return nums[:mid+1]

        if nums[-1]>target: nums = BST_remove_ele_greater_target()

        dp = [1] + [0] * (target)

        for t in range(1, target + 1):
            for num in nums:
                if num <= t: dp[t] += dp[t - num]
        return dp[-1]