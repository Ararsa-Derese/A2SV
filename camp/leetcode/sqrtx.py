class Solution:
    def mySqrt(self, x: int) -> int:
        l=1
        j=x
        while l<=j:
            mid=(l+j)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                l=mid+1
            else:
                j=mid-1
        return l-1