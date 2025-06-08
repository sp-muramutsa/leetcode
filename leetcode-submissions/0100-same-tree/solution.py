# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # If both nodes are None, they are identical
        if p is None and q is None:
            return True
        
        # If only one is None, they are not identical
        if p is None or q is None:
            return False
        
        # Recursively check if the left and the right sides of both trees are identical
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False # If their values are not identical why even bother.

