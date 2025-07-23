# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.same = True

        def preorder(node1, node2):

            if not node1 and not node2:
                return

            if not node1 or not node2:
                self.same = False
                return

            if node1.val != node2.val:
                self.same = False
                return

            preorder(node1.left, node2.left)
            preorder(node1.right, node2.right)

        preorder(p, q)
        return self.same

