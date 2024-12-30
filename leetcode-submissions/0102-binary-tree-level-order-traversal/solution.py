# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Cleaner recursive solution
# Intuition: Start on level 0
# Check the level. If it's a new level: Create a new list for it.
# Always append to the list on each iteration. You append each element to the sublist corresponding to its level.
# Time: O(n) -> Can be O(n^2) in a skewed tree
# Space: O(n) recursion stack space


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = []
        if not root:
            return traversal

        def helper(node, level):
            if len(traversal) == level:
                traversal.append([])

            traversal[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)

            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return traversal

