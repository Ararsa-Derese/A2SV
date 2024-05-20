# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm  = sum(nums)
        if sm%2:return 0
        sm /= 2
        di = {}
        def db(i,sm):
            if (i,sm) in di:return di[(i,sm)]
            if i==len(nums):return sm==0
            x= db(i+1,sm-nums[i]) or db(i+1,sm)
            di[(i,sm)] = x
            return x 
        return db(0,sm)