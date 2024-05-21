# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==1:
            return triangle[0][0]
        def inbound(i,j):
            return 0<=i<len(triangle) and 0<=j<len(triangle[i])
        dp = defaultdict(int)
        dp[(0,0)] = triangle[0][0]
        def check(i,j):
            if inbound(i,j):
                return dp[(i,j)]
            return float('inf')
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                dp[(i,j)] = triangle[i][j] + min(check(i-1,j),check(i-1,j-1))
        ans = float('inf')
        for i in range(len(triangle[len(triangle)-1])):
            ans = min(ans,dp[(len(triangle)-1,i)])
        return ans
                
