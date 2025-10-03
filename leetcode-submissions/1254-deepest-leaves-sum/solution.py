# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        values = deque([root.val])
        ans = sum(values)
        while queue:
            nodes_in_current_level = len(queue)
            ans = sum(values)
            
            for nodes in range(nodes_in_current_level):
                current_node = queue.popleft()
                values.popleft()
                
                if current_node.left:
                    queue.append(current_node.left)
                    values.append(current_node.left.val)
                if current_node.right:
                    queue.append(current_node.right)
                    values.append(current_node.right.val)
                    
        return ans
            
