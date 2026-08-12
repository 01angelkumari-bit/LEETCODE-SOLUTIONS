# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        length=1
        curr=head
        while curr.next:
            length+=1
            curr=curr.next
        k=k%length
        if k==0:
            return head
        curr.next=head  #make linked list circular
        steps=length-k
        new_tail=head
        for _ in range(1,steps):
            new_tail=new_tail.next
        new_head=new_tail.next
        new_tail.next=None

        return new_head

            
