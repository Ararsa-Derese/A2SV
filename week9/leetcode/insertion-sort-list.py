# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def insertion( key, head, c, i):
            if head.val == key and i == c:
                return
            insertion(key, head.next, c, i + 1)
            if head.val > key:
                temp = head.val
                head.val = head.next.val
                head.next.val = temp
        temp=head.next
        key= 0
        c = 1
        i = 0
        while temp is not None:
            key = temp.val
            insertion(key, head, c, i)
            c += 1
            temp = temp.next

        return head
                    