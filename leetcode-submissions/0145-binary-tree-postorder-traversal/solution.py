# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        traversal = []
        stack = []
        curr = root
        last_visited = root.val

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            peek = stack[-1]
            if peek.right and peek.right != last_visited:
                curr = peek.right

            else:
                node = stack.pop()
                traversal.append(node.val)
                last_visited = node

        return traversal

