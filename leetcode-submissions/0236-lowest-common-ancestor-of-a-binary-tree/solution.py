# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        def dfs(node, target):

            if not node:
                return False

            traversal.append(node)
            if node == target:
                return True

            if dfs(node.left, target):
                return True

            if dfs(node.right, target):
                return True

            traversal.pop()

        traversal = []
        dfs(root, p)
        A = traversal

        traversal = []
        dfs(root, q)
        B = traversal

        if len(A) < len(B):
            A, B = B, A

        lenA = len(A)
        lenB = len(B)
        seen = set(B)

        for i in range(lenB - 1, -1, -1):
            if A[i] in seen:
                return A[i]

        return

