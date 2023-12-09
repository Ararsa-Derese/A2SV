class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        ans=[]
        for p in paths:
            li=list(p.split())
            for i in range(1,len(li)):
                for j in range(len(li[i])):
                    if li[i][j]=="(":
                        dic[li[i][j+1:-1]].append(li[0]+"/"+li[i][:j])
        for key,val in dic.items():
            if len(val)>1:
                ans.append(val)
        return ans
            
                    
