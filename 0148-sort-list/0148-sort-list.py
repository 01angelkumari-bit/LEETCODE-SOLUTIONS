# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow,fast=head,head.next
        curr=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        left=head
        right=slow.next
        slow.next=None
        left=self.sortList(left)
        right=self.sortList(right)
        return self.mergedList(left,right)
    def mergedList(self,left:Optional[ListNode],right:Optional[ListNode])->Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        while left and right:
            if left.val<=right.val:
                curr.next=left
                left=left.next
            else:
                curr.next=right
                right=right.next
            curr=curr.next
        if left:
            curr.next=left
        else:
            curr.next=right
        return dummy.next
        