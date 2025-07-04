# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Edge cases if our root is None, we return None
        if root is None:
            return root
        # Traverse our binary tree using dfs method
        # Keep the left node as a temp variable
        tmp = self.invertTree(root.left)
        # Set the left to the traversed right side
        root.left = self.invertTree(root.right) 
        # set the right to left
        root.right = tmp
        return root
