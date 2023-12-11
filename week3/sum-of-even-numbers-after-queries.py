class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        dic={}
        sum=0
        ans=[]*len(queries)
        for n in nums:
            if n%2==0:
                sum+=n
        for q in queries:
            if (nums[q[1]]+q[0])%2==0:
                if nums[q[1]]%2==0:
                    sum+=q[0]
                else:
                    sum+=nums[q[1]]+q[0]
            else:
                if nums[q[1]]%2==0:
                    sum-=nums[q[1]]
            nums[q[1]]=nums[q[1]]+q[0]
            ans.append(sum)
                    
        return ans