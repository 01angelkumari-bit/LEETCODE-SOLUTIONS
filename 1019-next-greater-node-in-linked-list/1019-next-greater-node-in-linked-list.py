# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        def reverseList( head: Optional[ListNode]) -> Optional[ListNode]:
            prev=None
            curr=head
            while curr:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            return prev
        head=reverseList(head)
        ans=[]
        stack=[]
        curr=head
        while curr:
            while stack and stack[-1]<=curr.val:
                stack.pop()
              
            if stack:
                ans.append(stack[-1])
            else:
                ans.append(0)
            stack.append(curr.val)
            curr=curr.next
        ans.reverse()
        return ans
