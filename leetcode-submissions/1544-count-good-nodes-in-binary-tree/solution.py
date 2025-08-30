# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, num):
            nonlocal res
            if root is None:
                return 0
            
            if root.val >= num:
                num = root.val
                res += 1

            return (dfs(root.left, num) + dfs(root.right, num))

        dfs(root, float("-inf"))
        return res
