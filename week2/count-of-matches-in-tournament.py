class Solution:
    def numberOfMatches(self, n: int) -> int:
        sum=0
        while n>1:
            if n%2==0:
                sum+=n//2
                n//=2
               
            else:
                sum+=(n-1)//2
                n=((n-1)//2)+1
        return sum