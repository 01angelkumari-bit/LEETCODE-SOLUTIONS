# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head is None or head.next is None:
            return head
        prev=None
        curr=head
        new_head=head.next
        while curr and curr.next:
            first=curr
            second=curr.next
            nxt=second.next

            second.next=first
            first.next=nxt
            if prev:
                prev.next=second

            prev=first
            curr=nxt
        return new_head

        




            
        




