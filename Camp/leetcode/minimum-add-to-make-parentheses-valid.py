class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o=0
        c=0
        for st in s:
            if st=="(":
                o+=1
            else:
                if o>0:
                    o-=1
                else:
                    c+=1
                
        return (o+c)