class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans=0
        l=len(grid)
        c=list(zip(*grid))
        for i in range(l):
            for j in range(l):
                ans+= (min(max(grid[i][:l]),max(c[j][:l]))-grid[i][j])
        return ans