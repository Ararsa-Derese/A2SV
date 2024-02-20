class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        ans=0
        tasks.sort(key=lambda x:x[1]-x[0],reverse=True)
        s=0
        for i,j in tasks:
            if j>s:
                ans+=(j-s)
                s=j-i
            else:
                s-=i
        return ans