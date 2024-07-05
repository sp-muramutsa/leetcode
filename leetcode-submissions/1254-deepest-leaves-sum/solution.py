# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((root, 0))
        last_loc, tot = 0, 0
        while len(queue) != 0:
            curr, loc = queue.popleft()
            if loc != last_loc:
                tot = 0
                last_loc = loc
            tot += curr.val

            if curr.left:
                queue.append((curr.left, loc + 1))
            if curr.right:
                queue.append((curr.right, loc + 1))
        return tot
        
