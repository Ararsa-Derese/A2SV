class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q=deque()
        [q.append(i) for i in range(len(tickets))]
        ans=0
        while tickets[k]>0:
            tickets[q[0]]-=1
            if tickets[q[0]]==0:
                q.popleft()
            else:
                q.append(q.popleft())
            ans+=1
        return ans
            
