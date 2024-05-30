# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])

        def inbound(i,j):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[i]):
                return (matrix[i][j])
            else:
                return 0
        
       
        mx = float('-inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    matrix[i][j] = (min(inbound(i-1,j-1),inbound(i-1,j),inbound(i,j-1)))+1
                mx = max(mx,(matrix[i][j]))
         
       
        return mx ** 2
                
                