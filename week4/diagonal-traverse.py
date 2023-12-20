class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # f=0
        # m=0
        # n=0
        # ans=[]
        # while True:
        #     ans.appen(mat[m][n])
        #     if (n+m)%2==0:
        #         if n-1<0:
        #             if m+1>=len(mat[0]):
        #                 if 
        dic=defaultdict(list)
        ans=[]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                dic[i+j].append(mat[i][j])
        for j in dic:
            if j%2==0:
                dic[j].reverse()
            for i in dic[j]:
                ans.append(i)
        return ans



