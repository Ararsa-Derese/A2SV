class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k>=len(cardPoints):
            return sum(cardPoints)
        j=len(cardPoints)-1
        s=sum(cardPoints[:k])
        print(s)
        ans=0
        while k>=0:
            ans=max(ans,s)
            s-=cardPoints[k-1]
            s+=cardPoints[j]
            j-=1
            k-=1
        return ans
