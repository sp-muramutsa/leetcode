# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.balance = True

        def depth(node):

            if not node:
                return 0

            left_height = depth(node.left)
            right_height = depth(node.right)

            if abs(left_height - right_height) > 1:
                self.balance = False

            return 1 + max(left_height, right_height)

        depth(root)
        return self.balance

