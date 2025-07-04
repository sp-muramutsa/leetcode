# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Edge case
        if root is None:
            return []
        # Using BFS we will traverse our binary tree
        # Define the result list
        result = []
        # Define the queue
        queue = deque()
        # Add the root node to the queue
        queue.append(root)
        # While queue
        while queue:
            # Get the length of queue
            length = len(queue) - 1
            # pop the first node and add it to the result
            node = queue.popleft()
            # Add its right node first and then left node if they are not None
            result.append(node.val)
            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)
            # Itereate over the other nodes
            # pop the rest of the queu and adding the children
            print([i.val for i in queue])
            print(result)
            for i in range(length):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return result
