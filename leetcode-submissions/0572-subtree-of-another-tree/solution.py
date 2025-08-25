# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # For each node we will check if subTree would be a node
        # Implement a isSame function
        # Traverse the root tree and check for each node
        def isSame(r, s):
            if r is None and s is None:
                return True
            elif r is None and s is not None or r is not None and s is None:
                return False
            elif r.val != s.val:
                return False
            return isSame(r.left, s.left) and isSame(r.right, s.right)

        def isSubTree(root, sub):
            if root is None:
                return False

            if isSame(root, sub):
                return True

            return (isSubTree(root.left, sub) or isSubTree(root.right, sub))

        return isSubTree(root, subRoot)
