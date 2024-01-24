# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp=head.next
        head.next=None
        ptr=head
        while temp:
            if ptr.val!=temp.val:
                    ptr.next=temp
                    ptr=temp
                    temp=temp.next
                    ptr.next=None
            else:  
                temp=temp.next
        return head