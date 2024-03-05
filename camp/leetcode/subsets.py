class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        def subs(temp,idx):
            if len(temp)>len(nums):
                return
            ans.append(temp[:])
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
