# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        minimum, maximum = float("-inf"), float("inf")
        valid = True

        def f(node, minimum, maximum):

            if not node:
                return

            nonlocal valid
            if node.val <= minimum:
                valid = False
                return

            if node.val >= maximum:
                valid = False
                return

            f(node.left, minimum, node.val)
            f(node.right, node.val, maximum)
        
        f(root, minimum, maximum)
        return valid

