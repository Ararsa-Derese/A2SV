class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        c=capacity
        ans=-1
        for i in range(len(plants)):
            if c>=plants[i]:
                c-=plants[i]
                ans+=1
            else:
                ans+=(i*2)+1
                c=capacity
                c-=plants[i]
                
        return ans+1