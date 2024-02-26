class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: (x[0]-x[1]))
        sum=0
        c=1
        for i,j in costs:
            if c<=len(costs)//2:
                sum+=i
            else:
                sum+=j
            c+=1
        return sum