class Solution:
    def numberOfWays(self, s: str) -> int:
        ans=0
        a=0
        sum1=0
        sum2=0
        b=0
        c=0
        d=0
        ps1=[0]*len(s)
        ps2=[0]*len(s)
        for i in range(len(s)):
            if s[i]=='0':
                a+=1
            else:
                ps1[i]=a+sum1
                sum1+=a
        for i in range(len(s)):
            if s[i]=='1':
                b+=1
            else:
                ps2[i]=b+sum2
                sum2+=b
        for i in range(len(s)):
            c=max(c,ps1[i])
            d=max(d,ps2[i])
            if s[i]=='0':
                ans+=c
            else:
                ans+=d
        return ans