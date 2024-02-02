# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l=head
        p=head
        r=head
        lft=left
        c=right
        d=left
        if not head or right==left:
            return head
        while left-1:
            p=l
            l=l.next
            left-=1
        while right-1:
            r=r.next
            right-=1
        
        temp=l.next
        d+=1
        l.next=r.next
        ptr=l
        while temp and d<=c:
            # print(ptr.val)
            ptr=temp
            temp=temp.next
            d+=1
            if lft==1:
                ptr.next=head
                head=ptr
            else:
                ptr.next=l
                p.next=ptr
                # print(p.val)
                l=ptr
            # print(l.val)
        # r.next=l
        # p.next=r
        return head