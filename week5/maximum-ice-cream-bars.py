class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sum=0
        costs.sort()
        for i in range(len(costs)):
            sum+=costs[i]
            if sum==coins:
                return i+1
            elif sum>coins:
                return i
        return len(costs)