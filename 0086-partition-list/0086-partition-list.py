# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smalldummy=ListNode(-1)
        largedummy=ListNode(-1)
        small=smalldummy
        large=largedummy
        curr=head
        while curr:
            if curr.val < x:
                small.next=curr
                small=small.next
            else:
                large.next=curr
                large=large.next 
            curr=curr.next
        large.next=None
        small.next=largedummy.next
        return smalldummy.next
