class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0],reverse=True)
        ans=0
        for i in range(len(points)-1):
            ans=max(points[i][0]-points[i+1][0],ans)
        return ans