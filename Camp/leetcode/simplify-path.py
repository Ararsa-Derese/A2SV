class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        add=""
        ans=""
        for i in range(len(path)):
            if path[i]=="/" and add:
                if add==".." and stack:
                    stack.pop()
                    
                elif add!="." and add!="..":
                    stack.append(add)
                add=""
            elif path[i]!="/":
                add+=path[i]
       
        if add and add!="/":
            if add==".." and stack:
                stack.pop()
            elif add!="." and add!="..":
                stack.append(add)
        if not stack:
            return "/"
        stack.reverse()
        while stack:
            ans+=("/"+stack.pop())
            print(stack)
        return ans
                