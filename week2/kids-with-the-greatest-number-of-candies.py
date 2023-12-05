class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        maxim=max(candies)
        for c in candies:
            if c+extraCandies>=maxim:
                ans.append(True)
            else:
                ans.append(False)
        return ans
