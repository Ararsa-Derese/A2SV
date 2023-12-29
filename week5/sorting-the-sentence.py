class Solution:
    def sortSentence(self, s: str) -> str:
        li=s.split()
        ans=sorted(li,key=lambda x: int(x[-1]))
        ans = [s[:-1] for s in ans]
        return ' '.join(ans)
            