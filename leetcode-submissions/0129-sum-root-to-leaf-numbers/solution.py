# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        # Top to bottom traversing both left and right
        # Check the result when you get down
        # Use Menon's trick to append a new digit to the number
        # Solve it like 112. Path Sum
        # Pass the new digit in brackets so we don't have to
        # worry about cleaning it up when backtracking

        self.sum = 0

        def dfs(node, curr_number):

            if not node:
                return

            # Leaf
            if not node.left and not node.right:
                self.sum += (curr_number * 10) + node.val

            dfs(node.left, (curr_number * 10) + node.val)
            dfs(node.right, (curr_number * 10) + node.val)

        dfs(root, 0)
        return self.sum

