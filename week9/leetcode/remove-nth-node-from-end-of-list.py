# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        c=0
        temp=head
        while temp.next:
            c+=1
            temp=temp.next
        ptr=head
        a=0
        if c-n<0:
            return head.next
        while a!=(c-n):
            a+=1
            ptr=ptr.next
        ptr.next=ptr.next.next
        return head
