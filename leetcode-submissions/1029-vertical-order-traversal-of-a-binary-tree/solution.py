# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        - (row, col)
        - (0, 0)
        - left: (row + 1, col - 1)
        - right: (row + 1, col + 1)

        - if nodes are in the same column and row, sort them by value
            - when can this happen?

        - dfs + hashing
            - hashmap: defaultdict(list)

        dfs(node, row, col) -> starting at dfs(root, 0, 0):
            if not node:
                return

            hashmap[(row, col)].append(node.val)
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        0, 0:   1
        -1, 1:  2
        -2, 2:  4
        0, 2:   5, 6
        1, 1:   3
        2, 2:   7

        - min and max
        """

        hashmap = defaultdict(list)

        def dfs(node, row, col):
            if not node:
                return

            hashmap[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        minimum = min(hashmap.keys())
        maximum = max(hashmap.keys())
        columns = []

        for i in range(abs(minimum), -1, -1):
            columns.append(sorted(hashmap[-i]))

        for j in range(1, maximum + 1):
            columns.append(sorted(hashmap[j]))

        result = []
        for col in columns:
            col = sorted(col, key=lambda x: x[0])
            temp = [x for _, x in col]
            result.append(temp)

        return result

