class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def perm(temp,idx):
            if len(temp)==len(nums):
                ans.append(temp[:])
                return
            for i in range(len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    perm(temp,i+1)
                    temp.pop()
        temp=[]
        for i in range(len(nums)):
            temp.append(nums[i])
            perm(temp,i+1)
            temp.pop()
        return ans