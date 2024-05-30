# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(i, j):
            if i>=len(days):
                return 0
            if j >= days[i]:
                return dp(i+1, j)
            return min( dp(i+1, days[i])+costs[0], dp(i+1, days[i]+6)+costs[1],dp(i+1, days[i]+29)+costs[2])
        return dp(0,0)