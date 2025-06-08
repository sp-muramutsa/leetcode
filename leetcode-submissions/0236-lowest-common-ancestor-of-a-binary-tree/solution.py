# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":

        self.ancestors = [p]

        def getAncestors(root, target) -> list:

            if root is None:
                return False

            if root.val == target.val:
                return True

            # Either of the branches contain the target
            if getAncestors(root.left, target) or getAncestors(root.right, target):
                self.ancestors.append(root)
                return True

            return False

        getAncestors(root, p)
        p_ancestors = self.ancestors

        self.ancestors = [q]
        getAncestors(root, q)
        q_ancestors = set(self.ancestors)

        for x in p_ancestors:
            if x in q_ancestors:
                return x

