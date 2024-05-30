# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dfsStack = []
        direction = [(1,0) , (0,1) ]
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1 or obstacleGrid[0][0]:
            return 0
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]   
        dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1]=1
        def rec(i,j):
            if obstacleGrid[i][j]==1:
                return 0
            if dp[i][j] !=0:
                return dp[i][j]
            for x,y in direction:
                dx = i+x
                dy = j+y
                if 0<=dx<len(obstacleGrid) and 0<=dy<len(obstacleGrid[i]):
                   dp[i][j] += rec(dx,dy)
            return dp[i][j]
        rec(0,0)
        return dp[0][0]