# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values):
        @lru_cache(None)
        def dfs(i,j):
            if i>=j:
                return 0

            res = float("inf")

            for k in range(i,j):
                res = min(res,dfs(i,k) + dfs(k+1,j) + values[i-1]*values[k]*values[j])

            return res

        return dfs(1,len(values)-1)

        

