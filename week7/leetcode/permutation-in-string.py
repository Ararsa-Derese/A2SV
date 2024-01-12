class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1=Counter(s1)
        dic={}
        l=0
        for i in range(len(s2)):
            if s2[i] in dic:
                dic[s2[i]]+=1
            else:
                dic[s2[i]]=1
            if (i-l)+1==len(s1):
                if dic==dic1:
                    return True
                dic[s2[l]]-=1
                if dic[s2[l]]==0:
                    del dic[s2[l]]
                l+=1
        return False
           