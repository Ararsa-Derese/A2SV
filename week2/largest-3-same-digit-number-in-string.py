class Solution:
    def largestGoodInteger(self, num: str) -> str:
        dic={}
        c=0
        ch=num[0]
        maxim=-1
        ans=""
        f=0
        for n in num:
            if n==ch:
                c+=1
            else:
                if c>=3:
                    f=1
                    if int(ch)>maxim:
                        ans=""
                        maxim=max(int(ch),maxim)
                        ans+=str(maxim)*3
                c=1
                ch=n
       
        if c>=3:
            if int(ch)>maxim:
                ans=""
                ans+=str(max(int(ch),maxim))*3
        return ans
            