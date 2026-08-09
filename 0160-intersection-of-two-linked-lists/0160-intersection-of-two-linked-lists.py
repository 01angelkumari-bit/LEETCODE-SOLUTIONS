# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lA,lB=headA,headB
        while lA!=lB:
            if lA is not None:
                lA=lA.next
            else:
                lA=headB
            if lB is not None:
                lB=lB.next
            else:
                lB=headA
        return lB# or return lA
        
        
       

        