class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        ans=[]
        for n in nums:
            if n in dic:
                dic[n]+=1
            else:
                dic[n]=1
        for key,value in dic.items():
            if value>len(nums)/3:
                ans.append(key)
        return ans