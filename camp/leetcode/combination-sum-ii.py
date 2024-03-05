class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        if sum(candidates)<target:
            return []
        def calc(nums,i):
            # print(i)
            print(nums)
            # print(ans)
            if sum(nums)>target:
                return
            if sum(nums)==target:
                a=sorted(nums)
                if a not in ans:
                    ans.append(a[:])
                return
            p=nums[0]
            for k in range(i,len(candidates)): 
                if k>i and k<len((candidates)) and candidates[k]==p:
                    continue
                else:
                    p=candidates[k]                
                nums.append(candidates[k])
                calc(nums,k+1)
                nums.pop()
        nums=[]
        candidates.sort()
        prev=candidates[0]
        for i in range(len(candidates)):
                if i>0 and i<len((candidates)) and candidates[i]==prev:
                    continue
                else:
                    prev=candidates[i]
                nums.append(candidates[i])
                calc(nums,i+1)
                nums.pop()
        return ans