class Solution:
    def reverseWords(self, s: str) -> str:
        li=list(s.split())
        li.reverse()
        return " ".join(li)
