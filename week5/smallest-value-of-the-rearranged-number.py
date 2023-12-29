class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return 0
        ans="" 
        if num>0:
            li=sorted(list(str(num)))
            a=''.join(li)
                
            idx=li.count('0')
            ans+=li[idx]
            if idx:
                ans+="0"*idx
            ans+=a[idx+1:]
            ans=int(ans)
        else:
            li=sorted(list(str(num)),reverse=True)
            li.pop()
            ans=int(''.join(li))
            ans=ans-(ans*2)
        return ans

        
