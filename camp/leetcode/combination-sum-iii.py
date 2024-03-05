class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def comb(nums,idx):
            if len(nums)==k and sum(nums)==n:
                ans.append(nums[:])
                return
            if sum(nums)>n:
                return
            for i in range(idx,10):
                nums.append(i)
                comb(nums,i+1)
                nums.pop()
        nums=[]
        for i in range(1,10):
            nums.append(i)
            comb(nums,i+1)
            nums.pop()
        return ans