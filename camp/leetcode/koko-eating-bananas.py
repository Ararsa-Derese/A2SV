class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(num):
            a=0
            for k in range(len(piles)):
                a+=ceil(piles[k]/num)
            if a>h:
                return False
            return True
        i,j=1,sum(piles)
        while i<=j:
            mid=(i+j)//2
            if check(mid):
                j=mid-1
            else:
                i=mid+1
        return i


