# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_sum = [float("-inf")]

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            max_left = max(0, left)

            right = dfs(node.right)
            max_right = max(0, right)

            max_sum[0] = max(max_sum[0], node.val + max_left + max_right)

            return node.val + max(max_left, max_right)

        dfs(root)
        return max_sum[0]

