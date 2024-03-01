class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def calc(l,r):
            if l==r:
                return nums[l]
            left=nums[l]-calc(l+1,r)
            right=nums[r]-calc(l,r-1)
            return max(left,right)
        return calc(0,len(nums)-1)>=0