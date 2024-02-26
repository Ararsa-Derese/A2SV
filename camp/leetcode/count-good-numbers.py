class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def pw(c,a):
            if a == 1:
                return c
            if a < 1:
                return 1
            num = pw(c, a//2) % ((10**9)+7)
            if a%2:
                return (c * num * num ) %((10**9)+7)
            return  (num * num) % ((10**9)+7)


        return ((pw(5,n//2+(n%2))% ((10**9)+7)) * (pw(4,n//2))% ((10**9)+7))