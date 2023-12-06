class Solution:
    def totalMoney(self, n: int) -> int:
        r=n//7
        ans=0
        if n>7:
            for i in range(1,r+1):
                ans+=(28)+(7*(i-1))
            m=n%7
            ans+= (((1+((r+1)+(m-1)))*((r+1)+(m-1)))//2)-((1+r)*r)//2
        else:
            return ((1+n)*n)//2
        return ans