# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        same = True

        def dfs(p, q):
            if not p and not q:
                return

            nonlocal same
            if not p or not q:
                same = False
                return

            if p.val != q.val:
                same = False

            dfs(p.left, q.left)
            dfs(p.right, q.right)

        dfs(p, q)
        return same

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        self.same = False

        def dfs(node):
            if not node:
                return

            print(node.val, self.is_same_tree(node, subRoot))
            if self.is_same_tree(node, subRoot):
                self.same = True
                return

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.same

