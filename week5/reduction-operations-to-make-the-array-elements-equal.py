class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        maxm=nums[0]
        ans=0
        for i in range(len(nums)):
            if nums[i]!=maxm:
                ans+=i
                maxm=nums[i]
        return ans

      
        # dic=Counter(nums)
        # li=list(dic.values())
        # li.reverse()
        # ans=0
        # # sys.set_int_max_str_digits(9000)
        # for i in range(len(li)-1):
        #     ans += (li[i]) + ans
        # return ans