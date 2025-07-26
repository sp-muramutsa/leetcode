# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        hashmap = defaultdict(list)
        self.max_h = 0

        def reverse_height(node):

            if not node:
                return 0

            left_h = reverse_height(node.left)
            right_h = reverse_height(node.right)

            height = max(left_h, right_h)
            self.max_h = max(self.max_h, height)
            hashmap[height].append(node.val)

            return 1 + height

        reverse_height(root)
        result = []
        for i in range(self.max_h + 1):
            result.append(hashmap[i])

        return result

