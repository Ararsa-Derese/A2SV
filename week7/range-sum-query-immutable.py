class NumArray:

    def __init__(self, nums: List[int]):
        self.ps=[]
        self.ps.append(nums[0])
        for i in range(1,len(nums)):
            self.ps.append(self.ps[i-1]+nums[i])


    def sumRange(self, left: int, right: int) -> int:
        if left>0:
            return self.ps[right]-self.ps[left-1]
        return self.ps[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)