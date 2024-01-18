class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
         ps=[0]*1001
         for n,f,t in trips:
             ps[f]+=n
             ps[t]-=n
         sm=0
         for i in range(1001):
             sm+=ps[i]
             if sm>capacity:
                 return False
         return True