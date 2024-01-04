class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        closest = nums[0] + nums[1] + nums[2]
        nums.sort()
        for first in range(len(nums) - 2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                curSum = nums[first] + nums[second] + nums[third]
                if curSum == target:
                    return curSum
                if abs(target - curSum) < abs(target - closest):
                    closest = curSum
                if curSum > target:
                    third -= 1
                else:
                    second += 1
        return closest