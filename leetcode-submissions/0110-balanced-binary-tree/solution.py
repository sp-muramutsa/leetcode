# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.balance = True

        def helper(node):
            """
            Calculates the depth of two subtrees of the same node
            and checks if they differ by more than one node.
            """

            if not node:
                return 0

            left_depth = helper(node.left)
            right_depth = helper(node.right)

            if abs(left_depth - right_depth) > 1:
                self.balance = False

            return 1 + max(left_depth, right_depth)

        helper(root)
        return self.balance

