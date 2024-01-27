class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
             return ""
        dic={}
        dic1={}
        for c in t:
            dic[c]=1+ dic.get(c,0)

        a,b=0,len(dic)
        ans, maxm=[-1,-1],float('inf')
        l=0
        for i in range(len(s)):
            c=s[i]
            dic1[c]=1+dic1.get(c,0)

            if c in dic and dic1[c]== dic[c]:
                a+=1
            while a==b:
                if (i-l + 1) < maxm:
                    ans=[l,i]
                    maxm=(i-l+1)
                dic1[s[l]]-=1
                if s[l] in dic and dic1[s[l]]< dic[s[l]]:
                    a-=1
                l+=1
        l,r=ans
        return s[l:r+1] if maxm!= float('inf') else ""

