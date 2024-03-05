class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def gen(o,c,temp):
            if o<0 and c<0:
                return
            if len(temp) == (n*2):
                ans.append(''.join(temp[:]))
                return
            if o==c:
                if o>0:
                    temp.append('(')
                    gen(o-1,c,temp)
                    temp.pop()
            if o<c:
                if c>0:
                    temp.append(')')
                    gen(o,c-1,temp)
                    temp.pop()
                if o>0:
                    temp.append('(')
                    gen(o-1,c,temp)
                    temp.pop()
                
        temp=[]
        gen(n,n,temp)
        return ans