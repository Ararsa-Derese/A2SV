class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        a = set() 
        dic=defaultdict()
        for i in range(len(s)):
            dic[s[i]]=i
        for i in range(len(s)):
            if s[i] not in a:
                while stack and s[i] < stack[-1] and i < dic[stack[-1]]:
                    a.discard(stack.pop())
                a.add(s[i])
                stack.append(s[i])
        return ''.join(stack)
        
        
                 