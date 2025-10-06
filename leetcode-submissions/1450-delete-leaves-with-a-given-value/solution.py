# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:

        def delete(node, target):

            if not node:
                return None

            # Check children first to make it possible for the curr node to be a leaf later
            node.left = delete(node.left, target)
            node.right = delete(node.right, target)

            if not node.right and not node.left and node.val == target:
                return None

            return node

        return delete(root, target)
    

