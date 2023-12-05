class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums)==1 or nums==sorted(nums):
            return True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if i>0 and i<len(nums):
                    if nums[i-1]>nums[i+1]:

                        n=sorted(nums[:i+1]+nums[i+2:])
                        if nums[:i+1]+nums[i+2:]==n:
                            return True
                        break  
                         
                    
                n=sorted(nums[:i]+nums[i+1:])
                if nums[:i]+nums[i+1:]==n:
                    return True
                break   
        return False
        