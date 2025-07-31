# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        self.has_path_sum = False

        def dfs(node, curr_sum):
            if not node:
                return

            # Leaf node
            if not node.left and not node.right:
                if curr_sum + node.val == targetSum:
                    self.has_path_sum = True
                    return

            curr_sum += node.val
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

            curr_sum -= node.val

        dfs(root, 0)
        return self.has_path_sum

