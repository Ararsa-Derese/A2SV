class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        li=list(s)
        if len(li)<k:
            li.reverse()
            return ''.join(li)
        for i in range(0,len(s),2*k):
            li[i:i+k] = reversed(li[i:i+k])
        return ''.join(li)