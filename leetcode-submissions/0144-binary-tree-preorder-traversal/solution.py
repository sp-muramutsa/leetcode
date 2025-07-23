# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        traversal = []
        stack = []
        curr = root

        while stack or curr:

            while curr:
                stack.append(curr)
                traversal.append(curr.val)
                curr = curr.left

            curr = stack.pop()
            curr = curr.right

        return traversal

