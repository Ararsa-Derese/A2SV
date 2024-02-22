class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for st in s:
            if not stack:
                stack.append(st)
                continue
            if st==")":
                if stack[-1]=="(":
                    stack.pop()
                else:
                    return False
            elif st=="]":
                if stack[-1]=="[":
                    stack.pop()
                else:
                    return False
            elif st=="}":
                if stack[-1]=="{":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(st)
        if stack:
            return False
        return True
            