class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        self.ans = ""
        def check(st):
            counter = Counter(st)
            if all(counter[i.upper()] >=1 and  counter[i.lower()]>=1  for i in counter):
                self.ans = st
                return 1
        for i in range(len(s),-1,-1):
            for j in range(0,len(s)-i+1):
                if check(s[j:i+j]):return self.ans
        return ""