class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans=0
        while target>1:
            if not maxDoubles:
                return ans+target-1
            elif target%2!=0:
                target-=1
                ans+=1
            else:
                target//=2
                ans+=1
                maxDoubles-=1
        return ans