# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Inorder: Left - Root - Right

        # Iterative
        if not root:
            return []

        traversal = []
        stack = [root]
        curr = root

        while stack:

            while curr and curr.left:
                stack.append(curr.left)
                curr = curr.left

            curr = stack.pop()
            if curr:
                traversal.append(curr.val)
                curr = curr.right
                stack.append(curr)

        return traversal

