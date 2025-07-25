# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Edge cases where one tree can be empty, return False 
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        if p is None and q is None:
            return True
        # If the the values are differrent we return False 
        if p.val != q.val:
            return False
        # Traverse the left
        left = self.isSameTree(p.left, q.left)
        # Traverse the right
        right = self.isSameTree(p.right, q.right)
        return (left and right)
