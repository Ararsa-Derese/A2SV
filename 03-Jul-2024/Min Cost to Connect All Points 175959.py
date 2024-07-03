# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = [[0, 0]] + [[float('inf'), i] for i in range(1, len(points))]
        result = 0
        while distances:
            closest = min(distances)
            result += closest[0]
            x, y = points[closest[1]]

            closest[:] = distances[-1][:]
            distances.pop()

            for dist in distances:
                x2, y2 = points[dist[1]]
                dist[0] = min(dist[0], abs(x - x2) + abs(y - y2))
        return result