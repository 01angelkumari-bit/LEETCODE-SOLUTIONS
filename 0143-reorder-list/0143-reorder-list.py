# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        slow,fast=head,head
        curr=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        curr=slow.next
        slow.next=None

        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        left=head
        right=prev
        while right:
            next1=left.next
            next2=right.next
            left.next=right
            right.next=next1
            left=next1
            right=next2


        