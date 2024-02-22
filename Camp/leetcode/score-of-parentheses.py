class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        c=0
        ans=0
        for st in s:
            if st==")":
                while stack and stack[-1]!="(":
                    c+=stack[-1]
                    stack.pop()
                stack.pop()
                if c:
                    stack.append(2*c)
                    c=0
                else:
                    stack.append(1)
            else:
                stack.append("(")
        while stack:
            ans+=stack.pop()
        return ans

        "(()(()))"