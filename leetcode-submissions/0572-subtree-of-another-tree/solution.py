# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def similar(self, x, y):
        same = True

        def equality(x, y):
            nonlocal same
            if not x and not y:
                return

            if not x or not y:
                same = False
                return

            print(x.val, y.val)
            if x.val != y.val:
                print(x.val, y.val, same)
                same = False
                print(x.val, y.val, same)
                return

            equality(x.left, y.left)
            equality(x.right, y.right)

        equality(x, y)
        return same

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        sub = False

        def dfs(node):

            nonlocal sub
            if not node:
                return

            if self.similar(node, subRoot):
                sub = True

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return sub

