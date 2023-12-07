class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=''
        t=0
        for i,j in enumerate(s):
            if( t<len(spaces) and i==spaces[t]):
                t+=1
                ans += " "
            ans+=j
        return ans