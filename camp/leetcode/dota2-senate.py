class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d=deque()
        r=deque()
        for s in range(len(senate)):
            if senate[s]=="R":
                r.append([senate[s],s])
            else:
                d.append([senate[s],s])
        
        while d and r:
            if d[0][1]<r[0][1]:
                r.popleft()
                d[0][1]+=len(senate)
                d.append(d.popleft())
                if not r:
                    return "Dire"
            else:
                d.popleft()
                r[0][1]+=len(senate)
                r.append(r.popleft())
                if not d:
                    return "Radiant"
        return "Dire" if d else "Radiant"
        