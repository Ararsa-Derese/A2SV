# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = defaultdict(int)
        for i in range(1, len(piles) // 2 + 1):
            dp[i] = dp[i - 1] + max(piles[i] - piles[len(piles) - i], piles[len(piles) - i] - piles[i])
        return dp[len(piles) // 2] > 0