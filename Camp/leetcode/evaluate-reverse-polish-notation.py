class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            if t=="+":
                a=stack.pop()
                b=stack.pop()
                stack.append(b+a)
            elif t=="-":
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif t=="*":
                a=stack.pop()
                b=stack.pop()
                stack.append(b*a)
            elif t=="/":
                a=stack.pop()
                b=stack.pop()
                if b/a >0:
                    stack.append(floor(b/a))
                else:
                    stack.append(ceil(b/a))
            else:
                stack.append(int(t))
        return stack.pop()
            