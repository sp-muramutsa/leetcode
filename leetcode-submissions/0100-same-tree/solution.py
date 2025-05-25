# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l = []
        m = []
        def dfs(root, h):
            if root is None:
                return 
            left = dfs(root.left, h)
            h.append(left.val if left else None)
            h.append(root.val)
            right = dfs(root.right, h)
            h.append(right.val if right else None)
        dfs(p, l)
        dfs(q, m)
        print(m)
        print(l)
        if m == l:
            return True
        return False
