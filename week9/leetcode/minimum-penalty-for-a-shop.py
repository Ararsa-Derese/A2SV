class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y=customers.count('Y')
        n=0
        s=y+n
        ans=0
        for i in range(len(customers)):
            if customers[i]=='Y':
                y-=1
            else:
                n+=1
            if s>y+n:
                s=y+n
                ans=i+1
        return ans

