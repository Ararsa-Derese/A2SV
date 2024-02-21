class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s)
        ans=0
        f=True
        a=sorted(c.values(),reverse=True)
        print(a)
        for val in a:
            if f and val%2!=0:
                ans+=val
                f=False
            elif val%2==0:
                ans+=val
            else:
                ans+=val-1
        return ans