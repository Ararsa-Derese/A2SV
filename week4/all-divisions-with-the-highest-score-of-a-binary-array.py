class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        dic={}
        all=sum(nums)
        c=0
        for i in range(len(nums)+1):
            if i==len(nums):
               s=all-(i-c)+c
               if s in dic:
                  dic[s].append(i)
               else:
                   dic[s]=[i]
               break
           
            else:
                s=all-(i-c)+c
            if s in dic:
               dic[s].append(i)
            else:
               dic[s]=[i]
            if nums[i]==0:
                c+=1
     
        ans=max(dic)
        return dic[ans]
            
        
        