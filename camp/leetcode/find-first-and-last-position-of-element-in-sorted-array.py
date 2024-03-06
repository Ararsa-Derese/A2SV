class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i,j=0,len(nums)-1
        ans=[-1,-1]
        while i<=j:
            mid=(j+i)//2
            if nums[mid]==target:
                i=mid+1
                ans[1]=mid
            elif nums[mid]<target:
                i=mid+1
            else:
                j=mid-1
        i,j=0,len(nums)-1
        while i<=j:
            mid=(j+i)//2
            if nums[mid]==target:
                j=mid-1
                ans[0]=mid
            elif nums[mid]>target:
                j=mid-1
            else:
                i=mid+1
        return ans