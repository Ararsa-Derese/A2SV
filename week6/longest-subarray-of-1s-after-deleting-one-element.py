class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, j, count, mx = 0, 0, 0, 0
        flag = True

        while j < len(nums):
            if nums[j] == 0:
                flag = False
                count += 1
            
            if count < 1:
                j += 1
            elif count == 1:
                mx = max(mx, j - i + 1)
                j += 1
            else:
                if nums[i] == 0:
                    count -= 1
                i += 1
                j += 1

        if flag:
            return len(nums) - 1
        return mx - 1


