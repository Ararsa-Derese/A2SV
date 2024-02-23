class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        q=deque()
        l=0
        for r in range(len(nums)):
            while q and q[-1]<nums[r]:
                    q.pop()
            if not q or q[-1]>=nums[r]:
                q.append(nums[r])
            if (r-l)+1==k:
                ans.append(q[0])
                if q and q[0]==nums[l]:
                    q.popleft()
                l+=1
                
            
        return ans