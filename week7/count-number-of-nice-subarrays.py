class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = [0] * (len(nums) + 1)
        ans[-1] = 1
        distance = 1

        for i in range(len(nums) - 1, -1, -1):
            distance = 1 if nums[i] % 2 else distance + 1
            ans[i] = distance

        i = 0
        count = 0

        for j in range(len(nums)):
            if nums[j] % 2:
                k -= 1

            while k == 0:
                count += ans[j + 1]

                if nums[i] % 2:
                    k += 1

                i += 1

        return count