# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        # Binary search
        min_diff = float("inf")
        closest = root.val

        while root:

            diff = abs(root.val - target)
            if diff < min_diff:
                closest = root.val
                min_diff = diff
            elif diff == min_diff:
                closest = min(closest, root.val)
                min_diff = diff

            if root.val > target:
                root = root.left
            else:
                root = root.right

        return closest

