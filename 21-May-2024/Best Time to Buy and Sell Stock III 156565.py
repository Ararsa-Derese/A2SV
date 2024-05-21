# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = defaultdict(int)
        def rec(i,opt,cnt):
            if cnt>2:
                return 0
            if i>=len(prices):
                return 0
            if (i,opt,cnt) not in dp:
                if opt == 'B':
                    dp[(i,opt,cnt)] = max(rec(i+1,'S',cnt+1)-prices[i],rec(i+1,'B',cnt))
                else:
                    dp[(i,opt,cnt)] = max(rec(i+1,'B',cnt)+prices[i],rec(i+1,'S',cnt))
            return dp[(i,opt,cnt)]
        
        return rec(0,'B',0)