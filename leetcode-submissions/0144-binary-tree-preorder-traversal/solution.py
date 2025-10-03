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

        stack = [root]
        traversal = []
        curr = root

        while curr and stack:
            while curr:
                traversal.append(curr.val)
                stack.append(curr)
                curr = curr.left

            while stack:
                curr = stack.pop()
                if curr.right:
                    curr = curr.right
                    break

        return traversal

