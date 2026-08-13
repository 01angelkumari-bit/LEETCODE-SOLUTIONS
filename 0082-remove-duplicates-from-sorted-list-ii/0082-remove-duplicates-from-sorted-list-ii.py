# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        if head is None or head.next is None:
            return head
        while curr :
            duplicate=False
            while curr.next and curr.val==curr.next.val:
                duplicate=True
                curr=curr.next
            if duplicate:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return dummy.next


                