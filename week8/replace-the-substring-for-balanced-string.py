class Solution:
    def balancedString(self, s: str) -> int:
        dic = {}
        for c in s: dic[c] = 1 + dic.get(c, 0)
            
        ans = len(s)
        ii = 0
        for i, c in enumerate(s): 
            dic[c] -= 1
            while ii < len(s) and all(dic[x] <= len(s)//4 for x in dic): 
                ans = min(ans, i-ii+1)
                dic[s[ii]] += 1
                ii += 1
        return ans 