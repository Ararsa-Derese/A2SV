class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        stack2=[]
        ans=[-1]*len(nums)
        for i in range(0,len(nums)*2):
            i=i%len(nums)
            while stack and nums[i]>nums[stack[-1]]:
                ans[stack.pop()]=nums[i]
            stack.append(i)
        return ans
                