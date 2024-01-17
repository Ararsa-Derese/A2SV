class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c=nums.count(0)
        prod=1
        if c>1:
            return [0 for i in range(len(nums))]
        for i in range(len(nums)):
            prod*=nums[i]
        ans=[]
        p=1
        if c==1:
            for i in range(len(nums)):
                if nums[i]!=0:
                    p*=nums[i]
            for i in range(len(nums)):
                if nums[i]==0:
                    ans.append(p)
                else:
                    ans.append(0)
        else:
            for i in range(len(nums)):
                ans.append(prod//nums[i])
        return ans