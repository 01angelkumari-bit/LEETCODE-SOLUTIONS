# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        while fast and fast.next :
            slow=slow.next
            fast=fast.next.next
        prev=None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp

        left,right=head, prev
        maximum=0
        while right:
            ans=left.val+right.val
            maximum=max(ans,maximum)
            left=left.next
            right=right.next
        return maximum 



