class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        dic=defaultdict(list)
        ans=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
               dic[j].append(matrix[i][j])
        for key,val in dic.items():
            ans.append(val)
        return ans