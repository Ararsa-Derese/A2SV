class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=i
        for o in operations:
            nums[dic[o[0]]]=o[1]
            dic[o[1]]=dic[o[0]]
            del dic[o[0]]
        return nums
              