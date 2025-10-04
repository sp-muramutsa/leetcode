# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        queue = deque([root])
        minimum_subtract = float("inf")
        ans = root.val
        
        while queue:
            number_of_nodes = len(queue)
            
            for i in range(number_of_nodes):
                current_node = queue.popleft()
                
                if minimum_subtract > abs(target - current_node.val):
                    ans = current_node.val
                    minimum_subtract = abs(target - current_node.val)
                    
                elif minimum_subtract == abs(target - current_node.val):
                    ans = min(ans,current_node.val)
                    
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                    
        return ans
        
