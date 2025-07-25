# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # max path of a node is obtained by extending either the left branch or the right branch
        # we only care about positive values
        # We can only split the path once.

        self.max_sum = float("-inf")

        def dfs(node):
            "Post order"

            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            max_left_sum = max(left_sum, 0)
            max_right_sum = max(right_sum, 0)

            self.max_sum = max(self.max_sum, node.val + max_left_sum + max_right_sum)

            return node.val + max(max_left_sum, max_right_sum)

        dfs(root)
        return self.max_sum

