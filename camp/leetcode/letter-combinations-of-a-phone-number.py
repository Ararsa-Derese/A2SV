class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={'2':['a','b','c'], '3': ['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        ans=[]
        def comb(c,idx):
            if len(c)==len(digits):
                ans.append(''.join(c[:]))
                return
            for i in range(len(dic[digits[idx]])):
                c.append(dic[digits[idx]][i])
                comb(c,idx+1)
                c.pop()
        c=[]
        if not digits:
            return []
        for i in range(len(dic[digits[0]])):
            c.append(dic[digits[0]][i])
            comb(c,1)
            c.pop()
        return ans
