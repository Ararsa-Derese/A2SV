class Solution:
    def minimumSteps(self, s: str) -> int:
        ans=0
        c=0
        for st in s:
            if st=="1":
                c+=1
            else:
                ans+=c
        return ans