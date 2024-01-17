class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ps=[0 for i in range(n+2)]
        for f,l,s in bookings:
            ps[f]+=s
            ps[l+1]-=s
        _sum=0
        ans=[]
        for i in range(1,n+1):
            _sum+=ps[i]
            ans.append(_sum)
        return ans
