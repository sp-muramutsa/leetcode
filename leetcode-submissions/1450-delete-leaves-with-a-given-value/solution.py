# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        # Base case 
        if not root:
            return None

        # Check the node's children
        root.left = self.removeLeafNodes(root.left, target)

        root.right = self.removeLeafNodes(root.right, target)

        # Check the node itself.
        if not root.left and not root.right and root.val == target:
            return None

        return root

