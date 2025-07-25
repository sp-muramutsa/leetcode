# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        # Skill to practice here is forming a path that passes through any node. Not just root.
        # Going down:
        # We go down a path with a value equal to our current value

        # Backtracking
        # We choose the longest path that had the current value if any

        self.max_path_len = 0

        def dfs(prev, node):

            if not node:
                return 0

            left_path = dfs(node, node.left)
            right_path = dfs(node, node.right)

            self.max_path_len = max(self.max_path_len, left_path + right_path)

            # Coming back up
            if prev and prev.val == node.val:
                return 1 + max(left_path, right_path)
            else:
                return 0

        dfs(None, root)
        return self.max_path_len

