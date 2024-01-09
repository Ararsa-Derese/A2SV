class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        ans=0
        c=0
        while i<len(nums) and j<len(nums):
            if nums[j]==0:
                k-=1
            if k<0:
                while k<0:
                    if nums[i]==0:
                        k+=1
                        i+=1
                        c-=1
                    else:
                        c-=1
                        i+=1
            
            j+=1
            c+=1
            ans=max(ans,c)
        return ans
            