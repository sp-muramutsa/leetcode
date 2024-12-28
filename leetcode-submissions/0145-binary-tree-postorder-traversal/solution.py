# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative: REVERSE the result of a post order that goes right before left.
# Basically we do: ROOT-RIGHT-LEFT then reverse the result. Consult the notes for pre order solutions.
# Please remember .reverse() reverses the function inplace and returns None.

# Time: O(n)
# Space: O(h)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        current = root
        stack = []
        traversal = []

        while current or stack:
            while current:
                traversal.append(current.val)
                stack.append(current)
                current = current.right
            
            current = stack.pop()
            current = current.left
        
        traversal.reverse()
        return traversal
            
        
