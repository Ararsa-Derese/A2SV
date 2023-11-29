class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort(key=lambda x:len(x))
        ans=strs[0]
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                if j>=len(ans):
                    break
                if strs[i][j]!=ans[j]:
                    ans=ans[:j]
        return ans 
