class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max=0
        c=0
        
        for n in nums:
            if n==1:
                c+=1
            else:
                if max<c:
                   
                    max=c
                c=0
        if max<c:
            print(c)
            max=c
        return max
            