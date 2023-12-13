class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic={}
        ans=[]
        for c in range(len(cpdomains)):
            cp=list(cpdomains[c].split(" "))
            for j in range(len(cp[1])-1,-1,-1):
                if cp[1][j]==".":
                    if cp[1][j+1:] in dic:
                        dic[cp[1][j+1:]]+=int(cp[0])
                    else:
                        dic[cp[1][j+1:]]=int(cp[0])
            if cp[1] in dic:
                dic[cp[1]]+=int(cp[0])
            else:
                dic[cp[1]]=int(cp[0])
        for key, value in dic.items():
            ans.append(str(value)+" "+key)
        return ans
