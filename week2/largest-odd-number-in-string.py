class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans=""
        max=0
        sys.set_int_max_str_digits(10**5) 
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2==1:
                ans=num[:i+1]
                break
        return ans