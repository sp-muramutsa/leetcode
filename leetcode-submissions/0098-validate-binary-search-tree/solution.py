# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        lower, upper = float("-inf"), float("inf")
        stack = [(lower, root, upper)]

        while stack:

            lower, node, upper = stack.pop()

            if node.val <= lower or node.val >= upper:
                return False

            if node.left:
                stack.append((lower, node.left, node.val))

            if node.right:
                stack.append((node.val, node.right, upper))

        return True

