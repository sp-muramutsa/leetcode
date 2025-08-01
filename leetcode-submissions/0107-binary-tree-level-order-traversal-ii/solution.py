# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = deque([root])
        traversal = []

        while q:

            level = []
            k = len(q)

            for _ in range(k):
                node = q.pop()
                level.append(node.val)

                if node.left:
                    q.appendleft(node.left)

                if node.right:
                    q.appendleft(node.right)

            traversal.append(level)

        return traversal[::-1]

