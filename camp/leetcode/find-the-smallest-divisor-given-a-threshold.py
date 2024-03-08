class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        def check(num):
            sm = 0
            for i in range(len(nums)):
                sm += ceil(nums[i]/num)
            if sm <= threshold:
                print(sm)
                return True
            return False
        i,j = 1, nums[-1]
        ans=0
        while i <= j:
            mid = (i+j)//2
            if check(mid):
                j=mid-1
                ans=mid
            else:
                i=mid+1
        return ans