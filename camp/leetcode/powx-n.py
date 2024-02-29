class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=0
        def pw(c,a):
            if a == 1:
                return c
            if a < 1:
                return 1
            num = pw(c, a//2)
            if a%2:
                return (c * num * num ) 
            return  (num * num) 
        if n<0:
            return pw(1/x,abs(n))
        return pw(x,n)
