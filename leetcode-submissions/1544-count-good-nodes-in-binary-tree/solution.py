# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return []

        maximum = float("-inf")
        ans = 0

        def f(node, maximum):

            if not node:
                return

            if maximum <= node.val:
                nonlocal ans
                ans += 1

            maximum = max(maximum, node.val)
            f(node.left, maximum)
            f(node.right, maximum)
            maximum = min(maximum, node.val)

        f(root, float("-inf"))
        return ans

