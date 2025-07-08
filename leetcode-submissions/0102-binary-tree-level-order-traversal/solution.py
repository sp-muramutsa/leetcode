# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        dq = collections.deque([root])
        traversal = []

        while dq:
            level = []

            k = len(dq)
            for i in range(k):

                node = dq.popleft()
                level.append(node.val)

                if node.left:
                    dq.append(node.left)

                if node.right:
                    dq.append(node.right)

            traversal.append(level)

        return traversal

