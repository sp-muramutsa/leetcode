# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        curr = root
        stack = [root]

        while stack:
            k -= 1
            
            while curr:          
                stack.append(curr)
                curr = curr.left       
            
            curr = stack.pop()
            if k == 0:
                return curr.val
            curr = curr.right
           
