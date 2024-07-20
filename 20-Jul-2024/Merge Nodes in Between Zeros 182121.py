# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        current_new = dummy
        current = head.next
        sum_value = 0
        
        while current is not None:
            if current.val != 0:
                sum_value += current.val
            else:
                if sum_value != 0:
                    current_new.next = ListNode(sum_value)
                    current_new = current_new.next
                    sum_value = 0
            current = current.next
        
        return dummy.next