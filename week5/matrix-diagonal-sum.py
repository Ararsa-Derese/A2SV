class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        i=0
        j=0
        while i<len(mat) and j<len(mat):
            sum+=mat[i][j]
            i+=1
            j+=1
        i=len(mat)-1
        j=0
        while i>=0 and j<len(mat):
            sum+=mat[i][j]
            i-=1
            j+=1
        if len(mat)%2==1:
            sum-=mat[len(mat)//2][len(mat)//2]
        return sum
        