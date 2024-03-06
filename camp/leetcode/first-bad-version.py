# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i,j=0,n
        while i<j:
            mid=(j+i)//2
            if isBadVersion(mid):
                j=mid
            else:
                i=mid+1
        return j 