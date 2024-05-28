# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        dp={}
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            maxm=0
            for j in range(1,i):
                maxm=max(maxm, dp[i-j]*j, (i-j)*j)
            dp[i]=maxm
        
        return dp[n]