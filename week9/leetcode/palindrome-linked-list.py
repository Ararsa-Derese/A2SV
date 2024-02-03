# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: 
            return True
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            dummy = slow.next
            slow.next = prev
            prev = slow
            slow = dummy
        
        left = head
        right = prev
        while left and right:
            if left.val != right.val: return False
            left = left.next
            right = right.next
        return True
        