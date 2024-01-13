class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic={}
        f=0
        ans=len(cards)
        for i in range(len(cards)):
            if cards[i] in dic:
                f=1
                ans=min(ans,i-dic[cards[i]]+1)
                dic[cards[i]]=i
            else:
                dic[cards[i]]=i
        if f:
            return ans
        return -1