# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        #We are going to use the backtracking method where we use curr list to keep track of visited nodes.
        curr = []
        res = []
        #We create the dfs function which will store the res and modify curr as we visit nodes
        def dfs(node):
            #We identify the base case
            if node is None:
                return
            #We have reached the leaf node now we need to add to the solution
            curr.append(str(node.val))
            if node.left is None and node.right is None:
                res.append('->'.join(curr))
            else:
                dfs(node.left)
                dfs(node.right)
            #We backtrack as we have visited this node
            curr.pop()
        dfs(root)
        return res
