class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def get_next_position(nums, index, if_forward):
            direction = nums[index] >= 0
            
            if direction != if_forward:
                return -1
            
            next_index = (index + nums[index]) % len(nums)
            
            if next_index < 0:
                next_index += len(nums)
            
            if next_index == index:
                return -1
            
            return next_index


        if len(nums) <= 1:
            return False
        
        for i in range(len(nums)):
            slow = fast = i
            if_forward = nums[i] > 0
            
            while True:
                slow = get_next_position(nums, slow, if_forward)
                if slow == -1:
                    break
                
                fast = get_next_position(nums, fast, if_forward)
                if fast == -1:
                    break
                
                fast = get_next_position(nums, fast, if_forward)
                if fast == -1:
                    break
                
                if slow == fast:
                    return True
        
        return False

   