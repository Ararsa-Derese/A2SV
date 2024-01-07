class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=0
        r=0
        c=0
        ans=0
        vow=['a','e','i','o','u']
        while r<len(s) and l<len(s):
            if s[r] in vow:
                c+=1
            if r-l+1==k:
                ans=max(ans,c)
                if s[l] in vow:
                    c-=1
                l+=1
            
            r+=1
        return ans
            