# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next

        c = n // k
        cnt = n % k

        ans = []
        temp = head
        for i in range(k):
            ans.append(temp)
            curr = c + 1 if cnt > 0 else c
            cnt -= 1
            for j in range(curr - 1):
                temp = temp.next
            if temp:
                temp.next, temp = None, temp.next

        return ans