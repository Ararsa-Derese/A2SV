class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def comb(temp,idx):
            if sum(temp)>target:
                return
            if sum(temp)==target:
                ans.append(temp[:])
                return 
            temp.append(candidates[idx])
            comb(temp,idx)
            temp.pop()
            for i in range(idx+1,len(candidates)):
                temp.append(candidates[i])
                comb(temp,i)
                temp.pop()
        temp=[]
        for i in range(len(candidates)):
            temp.append(candidates[i])
            comb(temp,i)
            temp.pop()
        return ans