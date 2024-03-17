class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)-2):
            j = i + 1
            k = j + 1
            while k<len(nums):
                if nums[i]+nums[j]>nums[k]:
                    ans += (k-j)
                    k += 1
                else:
                    j += 1
                    if j == k:
                        k += 1
                
        return ans

