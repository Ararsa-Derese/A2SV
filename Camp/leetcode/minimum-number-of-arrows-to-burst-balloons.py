class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        mn=points[0][0]
        mx=points[0][1]
        ans=1
        for i,j in points:
            if (i<mn) and j<mn:
                mn=i
                ans+=1
            elif j>mx and i>mx:
                mx=j
                ans+=1
            elif i<mn:
                mn=i
            elif j>mx:
                j=mx
        return ans

