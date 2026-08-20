# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            leftheight=height(node.left)
            rightheight=height(node.right)

            if rightheight==-1 or leftheight==-1:
                return -1
            if abs(leftheight-rightheight)>1:
                return -1
            return 1+max(leftheight,rightheight)
            #either returns -1 or height of that node
        
        return height(root)!=-1   # 3!=-1--->true, if -1!=-1 --->return false