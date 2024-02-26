class Solution:
    def getRow(self, rowIndex: int, prev=[]) -> List[int]:
       
        if rowIndex==0:
            return [1]
        prev.append(self.getRow(rowIndex-1))
            
        res = [0] * (rowIndex + 1)
        
        res[0] = 1
        
        res[-1] = 1

        for j in range(1, len(res)-1):
            res[j] = prev[-1][j-1] + prev[-1][j]

        return res

        