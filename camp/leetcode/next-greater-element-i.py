class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        j=0
        dic=defaultdict()
        for i in range(len(nums1)):
            dic[nums1[i]]=i
        ans=[-1]*len(nums1)
        for i in range(len(nums2)):
            while stack and nums2[i]>stack[-1]:
                if stack[-1] in dic:
                    ans[dic[stack[-1]]]=nums2[i]
                stack.pop()
            stack.append(nums2[i])
        return ans

                    