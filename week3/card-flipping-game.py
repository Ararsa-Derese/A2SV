class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        rem=[fronts[i] for i in range(len(fronts)) if fronts[i]==backs[i]]
        
        min=float('inf')
        for i in range(len(fronts)):
            if fronts[i] not in rem:
                if fronts[i]<min:
                    min=fronts[i]
            if backs[i] not in rem:
                if backs[i]<min:
                    min=backs[i]

        if min in fronts or min in backs:
            return min
        else:
             return 0 
                                    