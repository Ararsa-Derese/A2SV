class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        k=0
        for n in nums:
            if n==0:
                i+=1
            elif n==1:
                j+=1
            else:
                k+=1
        for a in range(len(nums)):
            if i:
                nums[a]=0
                i-=1
            elif j:
                nums[a]=1
                j-=1
            else:
                nums[a]=2
                k-=1