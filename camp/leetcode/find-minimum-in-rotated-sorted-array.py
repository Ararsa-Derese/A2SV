class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if nums[0] < nums[-1]:
             return nums[0]
        i=0
        j=len(nums)-1
        ans=0
        while i<j:
            mid=i+(j-i)//2
            if nums[mid]>=nums[0]:
                i=mid+1
                ans=i
            else:
                j=mid
                ans=j
            
        return  nums[ans]