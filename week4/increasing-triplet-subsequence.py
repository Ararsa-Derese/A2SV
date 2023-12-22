class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        sm=float('inf')
        s=float('inf')
        for n in nums:
            if n<=sm:
                sm=n
            elif n<=s:
                s=n
            else:
                return True
        return False
        