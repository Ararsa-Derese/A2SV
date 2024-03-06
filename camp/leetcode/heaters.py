class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def check(nums):
            k=0
            l=0
            while k<len(houses) and l<len(heaters):
                if houses[k]>=heaters[l]-nums and houses[k]<=heaters[l]+nums:
                    k+=1
                else:
                    l+=1
            if l>=len(heaters) and k<len(houses):
                return False
            return True
        i,j=0,max(max(heaters),max(houses))
        while i<=j:
            mid=(i+j)//2
            if check(mid):
                j=mid-1
            else:
                i=mid+1
        return i