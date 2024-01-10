class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        dic=Counter(p)
        dic2={}
        l=0
        ans=[]
        for i in range(len(s)):
            if s[i] in dic2:
                dic2[s[i]]+=1
            else:
                dic2[s[i]]=1
            if (i-l)+1==k:
                if dic==dic2:
                    ans.append(l)
                dic2[s[l]]-=1
                if dic2[s[l]]==0:
                    del dic2[s[l]]
                l+=1
                
        return ans