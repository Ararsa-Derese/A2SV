class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic={}
        ans=[[],[]]
        for i in matches:
            if i[0] not in dic:
                dic[i[0]]=0
            if i[1] in dic:
                dic[i[1]]+=1
            else:
                dic[i[1]]=1
        for key, value in dic.items():
            if value==0:
                ans[0].append(key)
            elif value==1:
                ans[1].append(key)
        ans[0].sort()
        ans[1].sort()
        return ans