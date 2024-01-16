class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ps= [0 for i in range(len(s)+1)]
        for l, r , d in shifts:
            if d==0:
                ps[l]-=1
                ps[r+1]+=1
            else:
                ps[l]+=1
                ps[r+1]-=1
        sm=0
        ans=""
        for i in range(len(s)):
            sm+=ps[i]
            ans+=chr((((ord(s[i]) + sm) - 97) % 26) + 97)
        return ans