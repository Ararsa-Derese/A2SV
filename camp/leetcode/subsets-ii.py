class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        def subs(temp,idx):
            if len(temp)>len(nums):
                return
            a=sorted(temp)
            if a not in ans:
                ans.append(a)
            for i in range(idx,len(nums)):
                temp.append(nums[i])
                subs(temp,i+1)
                temp.pop()
        temp=[]
        for i in range(len(nums)):
            temp.append(nums[i])
            subs(temp,i+1)
            temp.pop()
        return ans