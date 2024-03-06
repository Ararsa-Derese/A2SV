class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mx=max(weights)
        i,j=mx,sum(weights)
        while i<=j:
            mid = (i+j)//2
            sm=0
            a=1
            for k in range(len(weights)):
                sm+=weights[k]
                if sm>mid:
                    sm=weights[k]
                    a+=1
            if a>days:
                i=mid+1
            else:
                j=mid-1
        return i