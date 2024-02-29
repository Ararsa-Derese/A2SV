class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        a=s[::-1]
        ans=[]
        lastidx=0
        part=0
        n=len(s)
        for i in range(n):
            lastidx=max(lastidx,n-a.index(s[i])-1)
            if i==lastidx:
                ans.append(i-part+1)
                part=i+1
                
        return ans
        
            