class Solution:
    def printVertically(self, s: str) -> List[str]:
        ar=s.split()
        maxim=len(max(ar,key=len))
        dic=defaultdict(list)
        k=0
        ans=[""]*maxim
        for i in range(len(ar)):
            if len(ar[i])<maxim:
                ar[i]+=" "*(maxim-len(ar[i]))
        for i in range(maxim):
            for j in range(len(ar)):
                ans[i]+=ar[j][i]
        for i in range(len(ans)):
            ans[i]=ans[i].rstrip()
        return ans
        


        