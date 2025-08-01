# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        columns = defaultdict(list)
        min_col, max_col = float("inf"), float("-inf")
        traversal = []

        dq = deque([(0, root)])

        while dq:
            k = len(dq)

            for _ in range(k):
                col, node = dq.popleft()
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                columns[col].append(node.val)

                if node.left:
                    dq.append((col - 1, node.left))

                if node.right:
                    dq.append((col + 1, node.right))

        for i in range(min_col, max_col + 1):
            traversal.append(columns[i])

        return traversal

