# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        def getHeight(node):
            global diameter

            if node is None:
                return 0

            left = getHeight(node.left)
            right = getHeight(node.right)
            self.diameter = max(self.diameter, left + right)

            return max(left, right) + 1

        getHeight(root)
        return self.diameter

