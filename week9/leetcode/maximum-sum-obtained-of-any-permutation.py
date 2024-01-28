class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ps = [0]*len(nums)
        for i, j in requests:
            ps[i] += 1
            if j + 1 < len(ps):
                ps[j+1] -= 1
        cur = 0
        for i in range(len(ps)):
            ps[i] += cur
            cur = ps[i]
        return sum(n * c for n, c in zip(sorted(nums, reverse=True), sorted(ps, reverse=True))) % (10 ** 9 + 7)