# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        ptr=node
        while ptr.next:
            ptr.val=ptr.next.val
            if not ptr.next.next:
                ptr.next=None
                break
            ptr=ptr.next
            
            

