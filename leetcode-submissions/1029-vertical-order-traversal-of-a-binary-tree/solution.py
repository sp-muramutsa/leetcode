# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        columns = defaultdict(list)
        min_col, max_col = float("inf"), float("-inf")

        stack = [(0, 0, root)]

        while stack:

            col, row, node = stack.pop()
            columns[col].append((row, node.val))

            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left:
                stack.append((col - 1, row + 1, node.left))

            if node.right:
                stack.append((col + 1, row + 1, node.right))

        traversal = []
        for i in range(min_col, max_col + 1):
            column = sorted(columns[i])
            values = [y for x, y in column]
            traversal.append(values)

        return traversal

