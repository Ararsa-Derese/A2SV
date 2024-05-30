# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l,r, lim = 0, 10**10, lcm(divisor1,divisor2)
        while l<r:
            m=(l+r)//2
            a=m-m//divisor1 >= uniqueCnt1
            b=m-m//divisor2 >= uniqueCnt2
            c = m-m//lim >= uniqueCnt1+uniqueCnt2
            if a and b and c:
                r=m
            else:
                l=m+1
        return l